from os import path
from jinja2 import FileSystemLoader, Environment

here = path.abspath(path.dirname(__file__))

''' Setup global variables '''
FILE_DIR = f"{here}/templates"
FILE_LOADER = FileSystemLoader(FILE_DIR)
TEMPLATE_DIR = Environment(loader=FILE_LOADER)
