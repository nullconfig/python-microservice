import json, os, sys
from flask import Flask, Response, request
from python_cli_framework import GithubApiBot

app = Flask(__name__)

''' 
Launch flask api

command: curl -s 127.0.0.1:8888/github/<username> | jq .
'''
@app.route("/github/<username>", methods=['GET', 'POST'])
def retrieve_api_data(username):
    user_ = request.view_args['username']
    pa = GithubApiBot(user_)
    output = pa.github_user()
    serialized = pa.serialize_data(output)
 
    return serialized

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8888))
    app.run(host="0.0.0.0", port=port)
