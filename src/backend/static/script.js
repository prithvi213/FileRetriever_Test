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
    .then(response => response.text())
    .then(data => {
        fetch('/terminal', {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json'
            }
        })
        .then(response => response.json())
        .then(data => {
            document.getElementById('data').innerHTML = data.content;
            console.log(data.content)
        })
        .catch(function(error) {
            // Handle error
            console.log(error);
        })
    })
    .catch(function(error) {
        // Handle error
        console.log(error);
    });
}