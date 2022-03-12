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

async function hash(data) {
    const dataUint8 = new TextEncoder().encode(data)
    const hashBuffer = await crypto.subtle.digest('SHA-256', dataUint8);
    // const hashArray = Array.from(new Uint8Array(hashBuffer));
    // console.log("HashArr=", hashArray)
    return new Uint32Array(new Uint8Array(hashBuffer).buffer.slice(0, 4))[0]
}

async function onSubmitToAdmin(form) {
    // const election_pk = form.elements.election_pk.value
    // console.log(election_pk)
    // const [e, N] = election_pk.split('$').map(x => BigInt(x))
    // console.log("Election PK:", e, N)
    const choice = form.elements.blinded_choice.value
    const admin_signing_pk = form.elements.admin_signing_pk.value
    const [signing_e, signing_N] = admin_signing_pk.split('$').map(x => BigInt(x))
    console.log("Signing PK:", signing_e, signing_N)
    // encrypt choice
    console.log("Choice=", choice)
    // const encrypted_choice = encryptInt(choice, e, N)
    // console.log("EncryptedChoice=", encrypted_choice)
    const electionID = form.elements.election_id.value
    const blinding_factor = getBlindingFactor(electionID, signing_N)
    console.log("BlindingFactor=", blinding_factor)
    // save encrypted_choice to cookie
    // pushChoice(electionID, encrypted_choice)
    pushChoice(electionID, choice)
    // add blind factor
    // let hashed_msg = await hash(encrypted_choice)
    // console.log("Hashed_msg=", hashed_msg)
    // const blinded_msg = modExp(blinding_factor, signing_e, signing_N) * BigInt(hashed_msg)
    const blindingFactorRaisedExpo = modExp(blinding_factor, signing_e, signing_N)
    console.log("BlindingFactorRaisedExpo=", blindingFactorRaisedExpo)
    const blinded_msg = blindingFactorRaisedExpo * BigInt(choice) % signing_N
    // const blinded_msg = blinding_factor * encrypted_choice
    console.log("BlindedMsg=", blinded_msg)
    form.elements.blinded_choice.value = blinded_msg
}

function onSubmitToBallot(form) {
    console.log("We enter submit to ballot")
    const election_pk = form.elements.election_pk.value
    console.log("Election PK=", election_pk)
    const [e, N] = election_pk.split('$').map(x => BigInt(x))
    console.log("Election PK:", e, N)
    const signing_N = BigInt(form.elements.signing_modulo.value)
    console.log("Signing N = ", signing_N)
    const electionID = form.elements.election_id.value
    blindingFactor = getBlindingFactor(electionID, signing_N)
    console.log("BlindingFactor=", blindingFactor)
    const blindedMsg = BigInt(form.elements.signed_choice.value)
    console.log("BlindedMsg=", blindedMsg)
    let blindingFactorInv = inverse(blindingFactor, signing_N)
    console.log("blindingFactorInv=", blindingFactorInv)
    if (blindingFactorInv < 0) {
        blindingFactorInv += signing_N
    }
    console.log("blindingFactorInv (After < 0)=", blindingFactorInv)
    const signature = blindedMsg * blindingFactorInv % signing_N
    console.log("SignedChoiceAfterRemovingBlinding = ", signature)
    form.elements.signed_choice.value = signature
    // set the encrypted choice from cookie in form
    const choice = popChoice(electionID)
    console.log("Choice=", choice)
    const encryptedChoice = encryptInt(choice, e, N)
    console.log("Encrypted Choice = ", encryptedChoice)
    form.elements.encrypted_choice.value = encryptedChoice
    // remove the cookie for blinding factor
    const name = `blinding_factor_${electionID}`
    document.cookie = `${name}=; SameSite=Strict; Path=/; Max-Age=-999999;`
    form.submit()
}

// N = 2599966643n
// e = 65537n
// d = 1060225073n
// m = 2n
// k = 417n
// expected_sig = modExp(m, d, N)
// console.log("expected_sig=", expected_sig)
// k_exp = modExp(k, e, N)
// console.log("k_exp=", k_exp)
// c = m*k_exp
// console.log("c=",c)
// c_prime = modExp(c, d, N)
// console.log("c_prime=", c_prime)
// k_inv = inverse(k, N)
// console.log("k_inv=", k_inv)
// if(k_inv < 0) k_inv += N
// console.log("k_inv=", k_inv)
// actual_sig = c_prime * k_inv % N
// console.log("actual_sig=", actual_sig)
// console.log(expected_sig === actual_sig)