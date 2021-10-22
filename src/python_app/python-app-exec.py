#!/usr/bin/env python
'''
Example python cli boilerplate

command: python python-app-exec.py get -u <username> | jq .

'''
import argparse, json, logging
from python_cli_framework import GithubApiBot

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def cmd_parser():
    ''' parse command line arguments passed in '''
    parser = argparse.ArgumentParser(description='Boilerplate cli interface')
    parser.add_argument('-u', '--username',
                        help="Retrieve data from upstream api interface",
                        required=True)
    parser.add_argument('get', metavar='get', type=str, nargs='+',
                         help="Retrieve data from upstream api interface")

    return parser.parse_args()

def main() -> None:
    args = cmd_parser()
    logger.info("App starting")

    if args.username and args.get:
        pa = GithubApiBot(args.username)
        output = pa.github_user()
        print(json.dumps(pa.serialize_data(output)))

if __name__ == "__main__":
    main()
