from flask import Flask, render_template, jsonify, request
import subprocess
import os

app = Flask(__name__)

'''@app.route('/')
def get_request():'''


'''@app.route('/', methods=['POST'])
def post_request():
    post_data = request.get_json()
    command = 'echo ' + post_data
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    print(result.stdout)'''

'''@app.route('/')
def execute_command(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)'''

@app.route('/terminal', methods=['GET', 'POST'])
def terminal():    
    if request.method == 'GET':
        pass
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
        print(data.stdout)
    return "Done"
    
@app.route('/')
def index():
    # Replace the command with the desired terminal command
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)