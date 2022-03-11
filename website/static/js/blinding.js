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
    return new Uint32Array(new Uint8Array(hashBuffer).buffer.slice(0,4))[0]
}

async function onSubmitToAdmin(form) {
    const election_pk = form.elements.election_pk.value
    console.log(election_pk)
    const [e, N] = election_pk.split('$').map(x => BigInt(x))
    console.log("Election PK:", e, N)
    const choice = form.elements.blinded_choice.value
    const admin_signing_pk = form.elements.admin_signing_pk.value
    const [signing_e, signing_N] = admin_signing_pk.split('$').map(x => BigInt(x))
    console.log("Signing PK:", signing_e, signing_N)
    // encrypt choice
    console.log("Choice=", choice)
    const encrypted_choice = encryptInt(choice, e, N)
    console.log("EncryptedChoice=", encrypted_choice)
    const electionID = form.elements.election_id.value
    const blinding_factor = getBlindingFactor(electionID, signing_N)
    console.log("BlindingFactor=", blinding_factor)
    // save encrypted_choice to cookie
    pushChoice(electionID, encrypted_choice)
    // add blind factor
    let hashed_msg = await hash(encrypted_choice)
    console.log("Hashed_msg=", hashed_msg)
    const blinded_msg = modExp(blinding_factor, signing_e, signing_N) * BigInt(hashed_msg)
    // const blinded_msg = blinding_factor * encrypted_choice
    console.log("BlindedMsg=", blinded_msg)
    form.elements.blinded_choice.value = blinded_msg
}

function onSubmitToBallot(form) {
    console.log("We enter submit to ballot")
    const signing_N = BigInt(form.elements.signing_modulo.value)
    console.log("Signing N = ", signing_N)
    const electionID = form.elements.election_id.value
    blindingFactor = getBlindingFactor(electionID, signing_N)
    console.log("BlindingFactor=", blindingFactor)
    const blindedMsg = BigInt(form.elements.signed_choice.value)
    console.log("BlindedMsg=", blindedMsg)
    // TODO: remove blinding factor from the signed choice
    form.elements.signed_choice.value = blindedMsg / blindingFactor
    console.log("SignedChoiceAfterRemovingBlinding = ", form.elements.signed_choice.value)
    // set the encrypted choice from cookie in form
    const encryptedChoice = popChoice(electionID)
    console.log("EncryptedChoice=", encryptedChoice)
    form.elements.encrypted_choice.value = encryptedChoice
    // remove the cookie for blinding factor
    const name = `blinding_factor_${electionID}`
    document.cookie = `${name}=; SameSite=Strict; Path=/; Max-Age=-999999;`
    form.submit()
}
