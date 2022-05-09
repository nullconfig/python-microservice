#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import find_packages, setup, Command
from os import path,system
import sys
from shutil import rmtree


# Name should consist only of ASCII letters, and underscores
NAME='python_app'
DESCRIPTION='boilerplate python application'
AUTHOR='nullconfig'
EMAIL='nullconfig@gmail.com'
VERSION='0.0.1'
REQUIRES_PYTHON = '>=3.6.0'
URL='https://github.com/nullconfig/python-microservice'
URL='https://github.com/nullconfig/python-microservice'
REQUIRED = [
   "Jinja2","requests","PyYAML"
]

here = path.abspath(path.dirname(__file__))

class PythonPackage(Command):
    '''
    This class runs when the python_package parameter is passed from the commandline.
    It will destroy any previous build.
    '''
    description = 'Build and publish the package.'
    user_options = []

    @staticmethod
    def status(s):
        ''' Prints things in bold. '''
        print(f'\033[1m{s}\033[0m')

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        try:
            self.status('Removing previous builds')
            # delete previous builds
            rmtree(path.join(here, 'dist'))

        except OSError:
            pass

        self.status('Building Source and Wheel distribution…')
        system(f'{sys.executable} setup.py sdist bdist_wheel')

        sys.exit()

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    author=AUTHOR,
    author_email=EMAIL,
    url=URL,
    long_description=open('README.md').read(),
    install_requires=REQUIRED,
    python_requires=REQUIRES_PYTHON,
    include_package_data=True,

    classifiers=[
        # https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],

    cmdclass={
        'python_package': PythonPackage
    }
)
