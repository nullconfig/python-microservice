import argparse

class AppCommandLine(object):
  '''
  GithubApiBot command line interface
  '''
  def app_cmd():
    ''' parse command line arguments passed in '''
    parser = argparse.ArgumentParser(description= "Boilerplate cli interface")
    parser.add_argument('-u', '--username', 
                        help="Retrieve data from upstream api interface", 
                        required=True)
    parser.add_argument('get',
                        help="Retrieve data from upstream api interface")

    return parser.parse_args()
