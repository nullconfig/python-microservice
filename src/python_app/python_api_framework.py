import os, json
from flask import Flask, Response, render_template
from python_app.python_app_framework import GithubApiBot
from python_app.metrics.python_app_metrics import setup_metrics
from prometheus_client import REGISTRY
from prometheus_client.openmetrics.exposition import generate_latest

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
    return render_template('metrics.j2', metrics=generate_latest(REGISTRY).decode())

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8888))
    app.run(host="0.0.0.0", port=port)
