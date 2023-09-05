let table_created = false;

function has_double_backslashes(filename) {
    const expr = /\\\\/;
    return expr.test(filename);
}

function submit_path() {
    const form = document.getElementById('submit-path');

    form.addEventListener('submit', function(event) {
        event.preventDefault();
    });

    const path_name = document.getElementById("path-name").value;
    const data = {
        command: "python3 commands.py localhost prithvi FileRetriever",
        path: path_name
    }

    // HTTP Post Request
    fetch('/submit-path', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.text())
    .then(data => {
        // HTTP GET Request
        fetch('/submit-path', {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json'
            }
        })
        .then(response => response.json())
        .then(data => {
            // Get the terminal content and split into 2 lists: headers and data
            const data_content = data.content;
            const split_table = data_content.split('\n');
            split_table.pop();
            
            // Parse headers
            const header_string = split_table[0];
            const valid_header_string = header_string.replace(/'/g, '"');
            const headers = JSON.parse(valid_header_string);
            
            var table = document.getElementById('data-table');

            if(!table_created) {
                var header_row = document.createElement('tr');
                
                // Create the headers for the table
                headers.forEach((header) => {
                    var header_cell = document.createElement('th');
                    header_cell.textContent = header;
                    header_row.appendChild(header_cell);
                })
            
                // Append headers row to table
                table.appendChild(header_row);
                table_created = true;
            }
            
            while(table.rows.length > 1) {
                table.deleteRow(1);
            }

            var filedata_array = split_table[1];
            filedata_array = filedata_array.split("), (").join("):(").substring(1, filedata_array.length - 1).split(':');
            filedata_array[filedata_array.length - 1] = filedata_array[filedata_array.length - 1].slice(0, -1);
            
            filedata_array.map(function(element) {
                var parsed_tuple = element.slice(1, -1).split(", ");
                var filename = parsed_tuple[0].slice(1, -1);
                var filesize = parseInt(parsed_tuple[1]);
                var directory = parsed_tuple[2].slice(1, -1);

                if(has_double_backslashes(filename)) {
                    filename = filename.replace(/\\\\/g, "\\");
                }

                var row = document.createElement('tr');
                var filename_element = document.createElement('td');
                filename_element.textContent = filename;
                row.appendChild(filename_element);

                var filesize_element = document.createElement('td');
                filesize_element.textContent = filesize;
                row.appendChild(filesize_element);

                var directory_element = document.createElement('td');
                directory_element.textContent = directory;
                row.appendChild(directory_element);

                table.appendChild(row);
            });

            var file_count = table.querySelectorAll('tr').length - 1;
            var count_elem = document.getElementById('count');
            count_elem.textContent = 'File Count: ' + file_count;
        })
        .catch(function(error) {
            // Handle error
            console.log(error);
        })
    })
    .catch(function(error) {
        // Handle error
        console.log(error);
    })

}