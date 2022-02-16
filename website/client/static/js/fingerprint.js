const fpPromise = import('https://openfpcdn.io/fingerprintjs/v3')
    .then(FingerprintJS => FingerprintJS.load())

fpPromise
    .then(fp => fp.get())
    .catch(error => console.error(`Failed to get fingerprint \nError:${error}`))
    .then(result => {
        generateFingerprint(window.location.href + "api/fingerprint/", result.visitorId)
    })
    .catch(error => console.error(`Failed to store fingerprint \nError:${error}`))

function generateFingerprint(url, visitorId) {
    fetch(url, {
        method: 'POST',
        mode: 'same-origin',
        cache: 'no-store',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(visitorId)
    }).catch(error => console.error("Failed to setup fingerprint!"))
}