import os
import subprocess
from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def pull():
    print request
    _event = request.get_json()
    if _event == None:
        return "Request body invalid."
    try:
        repo_name = _event['repository']['name']
    except KeyError, e:
        print e
        print "Unexpected request payload: " + _event

    cwd = os.path.join(os.getcwd(), repo_name)
    print cwd
    subprocess.Popen(['sudo', 'git', 'pull'], cwd=cwd)
    return "Successfully updated '%s'" % cwd

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6969)
