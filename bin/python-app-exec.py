#!/usr/bin/env python
'''
Example python cli boilerplate
'''

import json
from python_app.python_app_framework import GithubApiBot as bot
from python_app.python_cli_framework import AppCommandLine as cli

def main() -> None:
    if cli.app_cmd().username and cli.app_cmd().get:
        output = bot(cli.app_cmd().username).github_user()

    print(json.dumps([i['name'] for i in output]))

if __name__ == "__main__":
    main()
