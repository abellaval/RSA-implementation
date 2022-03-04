function fetchResults(election_id) {
    fetch(`/api/refresh_results/?election_id=${election_id}`, {
            method: 'GET',
            mode: 'same-origin',
            cache: 'no-store',
            headers: {
                'Content-Type': 'application/json'
            }
        }
    ).then(response => response.json()
    ).then(data => {
        Object.entries(data).forEach(entry => {
            const [key, val] = entry
            document.getElementById(key).innerText = val
        })
    })
}