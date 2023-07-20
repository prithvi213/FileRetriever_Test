from flask import Flask, render_template, jsonify, request, make_response
import subprocess
import os

app = Flask(__name__)

@app.route('/terminal', methods=['GET', 'POST'])
def terminal():    
    if request.method == 'GET':
        with open("data.txt", "r") as file:
            content = file.read()
            body = {"content": content}
            response = make_response(body)
            print(response)
            response.headers['Content-Type'] = request.headers['Content-Type']
            c = response.data.decode('utf-8')
            print(c)
            return response
            #return jsonify(content)
    else:
        absolute_file_path = '/Users/prithvi/Library/CloudStorage/OneDrive-Personal/desktop_clutter/FileRetriever_Test/src/backend'
        os.chdir(absolute_file_path)
        clean_cmd = ['make', 'clean']
        make_cmd = ['make', 'all']
        execute_cfile = ['./fileretriever']

        json_data = request.get_json()
        python_cmd = json_data['command']
        execute_pythonfile = python_cmd.split(' ')
        
        subprocess.run(clean_cmd, check=True)
        subprocess.run(make_cmd, check=True)
        subprocess.run(execute_cfile, check=True)
        data = subprocess.run(execute_pythonfile, check=True, capture_output=True)

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