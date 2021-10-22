#!/usr/bin/env python
'''
Example python cli boilerplate
'''

import argparse, json
from python_app import python_cli_framework as pcf

def cmd_parser():
    ''' parse command line arguments passed in '''
    parser = argparse.ArgumentParser(description='Boilerplate cli interface')
    parser.add_argument('-u', '--username', 
                        help="Retrieve data from upstream api interface", 
                        required=True)
    parser.add_argument('get',
                        help="Retrieve data from upstream api interface")

    return parser.parse_args()

def main() -> None:
    args = cmd_parser()

    if args.username and args.get:
        pa = pcf.GithubApiBot(args.username).github_user()
        print(json.dumps(pa))

if __name__ == "__main__":
    main()