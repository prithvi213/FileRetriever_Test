function handleClick() {

    // Payload
    var data = {
        command: "python3 commands.py parunsha Ha\!l0w3en3rrr encryption33link"
    }

    // HTTP Post Request
    fetch('/terminal', 
    {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(function(response) {
        // Handle response
        
    })
    .catch(function(error) {
        // Handle error
        console.log(error);
    });
}