import json, requests
import logging
from .global_variables import TEMPLATE_DIR, YAMLFILE
from urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class GithubApiBot(object):
  '''
  GithubApiBot
  '''
  def __init__(self, username):
    self.username = username

  def github_user(self) -> json:
    ''' Takes the username passed in at instantiation, and returns all of the repos found. '''
    return json.dumps(requests.get(f"https://api.github.com/users/{self.username}/repos").json())

  def consul_register(self, data) -> None:
    ''' Registers any data received to consul '''
    requests.put(f'http://127.0.0.1:8500/v1/catalog/register', data=data)

  def serialize_data(self, data) -> json:
    ''' Consul normalizer '''
    repos = self.repos
    repos_list = []
    user_dict = {"username": self.username, "repos_list": repos_list}
    template = TEMPLATE_DIR.get_template('dictionary_template.j2')

    if self.username in YAMLFILE['accounts']:
      logger.info(f"User works {YAMLFILE['accounts'][self.username]['company']}")
      logger.info("Generating a list of known public repos")
      for repos_found in repos:
        edited_string = json.dumps(repos_found['name']).replace('"', "")
        user_dict['repos_list'].append(edited_string)

      jinja_output = template.render(repos=user_dict)
 
      return json.loads(jinja_output)
