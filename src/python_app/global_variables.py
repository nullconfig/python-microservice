import yaml
from jinja2 import FileSystemLoader, Environment

''' Setup global variables '''
FILE_DIR = "./templates"
FILE_LOADER = FileSystemLoader(FILE_DIR)
TEMPLATE_DIR = Environment(loader=FILE_LOADER)

ymlfile = open(f"{FILE_DIR}/accounts.yml", "r").read()
YAMLFILE = yaml.safe_load(ymlfile)
