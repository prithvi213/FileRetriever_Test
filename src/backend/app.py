from flask import Flask, render_template, jsonify, request, make_response
import subprocess
import os

app = Flask(__name__)

@app.route('/submit-path', methods=['GET', 'POST'])
def submit_path():
    # GET Request
    if request.method == 'GET':
        # open and read the data file
        with open("data.txt", "r") as file:
            content = file.read()
            
            # store content in msg body and create the response
            body = {"content": content}
            response = make_response(body)
            response.headers['Content-Type'] = request.headers['Content-Type']
            return response
        
    # POST Request
    else:
        # Set file path and execute fundamental make commands
        absolute_file_path = '/Users/prithvi/Library/CloudStorage/OneDrive-Personal/desktop_clutter/FileRetriever_Test/src/backend'
        os.chdir(absolute_file_path)
        json_data = request.get_json()
        path_name = json_data['path']
        clean_cmd = ['make', 'clean']
        make_cmd = ['make', 'all']
        execute_cfile = ['./fileretriever', path_name]

        python_cmd = json_data['command']
        execute_pythonfile = python_cmd.split(' ')
        
        subprocess.run(clean_cmd, check=True)
        subprocess.run(make_cmd, check=True)
        subprocess.run(execute_cfile, check=True)

        # Store terminal output after running python file (commands.py)
        data = subprocess.run(execute_pythonfile, check=True, capture_output=True)
        #subprocess.run(execute_pythonfile, check=True)

        # Write terminal output to a textfile and parse response data before sending it over
        with open("data.txt", "w") as file:
            file.write(data.stdout.decode('utf-8'))

        response_data = {'OK': 200}
        response = jsonify(response_data)
        return response

    
@app.route('/')
def index():
    # Replace the command with the desired terminal command
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)