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

function getBlindingFactor(electionID, choice) {
    const name = `blinding_factor_${electionID}`
    let rngValStr = document.cookie.match("(^|;)\\s*" + name + "\\s*=\\s*([^;]+)")?.pop() || ''
    let rngVal;
    if (rngValStr === '') {
        // create the blinding factor and save it
        const val = new BigInt64Array(1)
        let is_coprime = false
        while (!is_coprime) {
            window.crypto.getRandomValues(val)
            rngVal = val[0]
            if (gcd(BigInt(choice), rngVal) === 1n) {
                is_coprime = true
            }
        }
        document.cookie = `${name}=${rngVal}`
    } else {
        rngVal = parseInt(rngValStr)
    }
    return rngVal
}

function onSubmitToAdmin(form) {
    const election_pk = form.elements.election_pk.value
    console.log(election_pk)
    const [e, N] = election_pk.split('$').map(x => BigInt(x))
    console.log(e,N)
    const choice = form.elements.blinded_choice.value
    // encrypt choice
    const encrypted_choice = encryptInt(choice, e, N)
    // TODO: add blind factor
    // const electionID = form.elements.election_id.value
    // const blinding_factor = getBlindingFactor(electionID, encrypted_choice)
    // add blind factor
    // form.elements.blinded_choice.value = modExp(encrypted_choice, blinding_factor, N)
    form.elements.blinded_choice.value = encrypted_choice
}

function onSubmitToBallot(form) {
    // blinding_factor = getBlindingFactor()
    // TODO: remove blinding factor from the signed choice
    // form.elements.signed_choice.value /= blinding_factor
}
