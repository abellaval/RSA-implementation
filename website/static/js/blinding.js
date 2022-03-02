function getBlindingFactor() {
    const name = "blinding_factor"
    let rngValStr = document.cookie.match("(^|;)\\s*" + name + "\\s*=\\s*([^;]+)")?.pop() || ''
    let rngVal;
    if (rngValStr === '') {
        // create the blinding factor and save it
        const val = new BigUint64Array(1)
        window.crypto.getRandomValues(val)
        rngVal = val[0]
        document.cookie = `${name}=${rngVal}`
    } else {
        rngVal = parseInt(rngValStr)
    }
    return rngVal
}

function onSubmit(form) {
    form.elements.blinded_choice.value *= getBlindingFactor()
}
