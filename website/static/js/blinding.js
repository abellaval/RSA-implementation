function modExp(x, e, n) {
    x = BigInt(x)
    e = BigInt(e)
    n = BigInt(n)
    let result = 1n
    while (true) {
        if (e & 0b1n) {
            result = (result * x) % n
        }
        if (e === 1n) {
            return result
        }
        x = (x * x) % n
        e >>= 1n
    }
}

function encryptInt(msg, e, N) {
    return modExp(msg, e, N)
}

function gcd(a, b) {
    if (!b) return a
    return gcd(b, a % b)
}

function euclide(a, b, u0 = 1n, v0 = 0n, u1 = 0n, v1 = 1n) {
    a = BigInt(a)
    b = BigInt(b)
    if (b === 1n) return [u1, v1]
    return euclide(b, a % b, u1, v1, u0 - u1 * (a / b), v0 - v1 * a / b)
}

function inverse(x, n) {
    return euclide(x, n)[0]
}

function getBlindingFactor(electionID, N) {
    const name = `blinding_factor_${electionID}`
    let rngValStr = document.cookie.match("(^|;)\\s*" + name + "\\s*=\\s*([^;]+)")?.pop() || ''
    let rngVal;
    if (rngValStr === '') {
        // create the blinding factor and save it
        let is_coprime = false
        while (!is_coprime) {
            rngVal = Math.floor(2 + Math.random() * 1000)
            if (gcd(BigInt(N), BigInt(rngVal)) === 1n) {
                is_coprime = true
            }
        }
        document.cookie = `${name}=${rngVal}; SameSite=Strict; Path=/;`
    } else {
        rngVal = parseInt(rngValStr)
    }
    return BigInt(rngVal)
}

function pushChoice(electionID, choice) {
    const name = `encrypted_choice_${electionID}`
    document.cookie = `${name}=${choice}; SameSite=Strict; Path=/;`
}

function popChoice(electionID) {
    const name = `encrypted_choice_${electionID}`
    const choice = document.cookie.match("(^|;)\\s*" + name + "\\s*=\\s*([^;]+)")?.pop() || ''
    document.cookie = `${name}=; SameSite=Strict; Path=/; Max-Age=-999999;`
    return parseInt(choice)
}

async function onSubmitToAdmin(form) {
    const choice = form.elements.blinded_choice.value
    const admin_signing_pk = form.elements.admin_signing_pk.value
    const [signing_e, signing_N] = admin_signing_pk.split('$').map(x => BigInt(x))
    // encrypt choice
    const electionID = form.elements.election_id.value
    const blinding_factor = getBlindingFactor(electionID, signing_N)
    // save choice to cookie
    pushChoice(electionID, choice)
    // add blind factor
    const blindingFactorRaisedExpo = modExp(blinding_factor, signing_e, signing_N)
    form.elements.blinded_choice.value = blindingFactorRaisedExpo * BigInt(choice) % signing_N
}

function onSubmitToBallot(form) {
    const election_pk = form.elements.election_pk.value
    const [e, N] = election_pk.split('$').map(x => BigInt(x))
    const signing_N = BigInt(form.elements.signing_modulo.value)
    const electionID = form.elements.election_id.value
    const blindingFactor = getBlindingFactor(electionID, signing_N)
    const blindedMsg = BigInt(form.elements.signed_choice.value)
    let blindingFactorInv = inverse(blindingFactor, signing_N)
    if (blindingFactorInv < 0) {
        blindingFactorInv += signing_N
    }
    form.elements.signed_choice.value = blindedMsg * blindingFactorInv % signing_N
    // set the encrypted choice from cookie in form
    const choice = popChoice(electionID)
    form.elements.encrypted_choice.value = encryptInt(choice, e, N)
    // remove the cookie for blinding factor
    const name = `blinding_factor_${electionID}`
    document.cookie = `${name}=; SameSite=Strict; Path=/; Max-Age=-999999;`
    form.submit()
}