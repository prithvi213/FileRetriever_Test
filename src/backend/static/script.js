function handleClick() {

    // Payload
    var data = {
        command: "python3 commands.py parunsha Ha\!l0w3en3rrr encryption33link"
    }

    // HTTP Post Request
    fetch('/terminal', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        fetch('/terminal', {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json'
            }
        })
        .then(response => response.json())
    })
    .catch(function(error) {
        // Handle error
        console.log(error);
    });
}