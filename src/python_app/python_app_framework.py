import json, requests
import logging
from python_app.global_variables import TEMPLATE_DIR
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
    return requests.get(f"https://api.github.com/users/{self.username}/repos").json()

  def consul_register(self, data) -> None:
    ''' Registers any data received to consul '''
    requests.put(f"http://127.0.0.1:8500/v1/catalog/register", data=data)

  def serialize_data(self, data) -> json:
    ''' Consul normalizer '''

    user_dict = {"username": self.username, "repos_list": [i['name'] for i in data]}
    template = TEMPLATE_DIR.get_template('dictionary_template.j2')
    jinja_output = template.render(repos=user_dict)
 
    return json.loads(jinja_output)
