import os
from flask import Flask, Response, request, render_template
from python_app.python_app_framework import GithubApiBot
from helpers.middleware import setup_metrics
import prometheus_client

CONTENT_TYPE_LATEST = str('text/plain; version=0.0.4; charset=utf-8')

app = Flask(__name__)
setup_metrics(app)

''' 
Launch flask api

command: curl -s 127.0.0.1:8000/github/<username> | jq .
'''

@app.route("/")
def main():
    return render_template('homepage.j2')

@app.route("/github/<username>", methods=['GET'])
def retrieve_api_data(username):
    pa = GithubApiBot(username)
    output = pa.github_user()

    serialized = pa.serialize_data(output)

    return serialized

@app.route("/metrics")
def metrics():
    return Response(prometheus_client.generate_latest(), mimetype=CONTENT_TYPE_LATEST)

if __name__ == '__main__':
    app.run()