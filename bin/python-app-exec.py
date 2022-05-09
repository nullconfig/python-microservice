#!/usr/bin/env python
'''
Example python cli boilerplate
'''

from python_app import python_app_framework as app
from python_app import python_cli_framework as cli

def main() -> None:
    args = cli.AppCommandLine.app_cmd()

    if args.username and args.get:
        print(app.GithubApiBot(args.username).github_user())

if __name__ == "__main__":
    main()
