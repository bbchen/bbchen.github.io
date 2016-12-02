from fabric.api import *
import fabric.contrib.project as project
import os
import sys
import datetime
import re
import codecs
from datetime import date, datetime
from unicodedata import normalize
from argh import *


# Local path configuration (can be absolute or relative to fabfile)

env.deploy_path = 'public'
env.content_path = 'content'
DEPLOY_PATH = env.deploy_path
CONTENT_PATH = env.content_path

env.github_address = "https://github.com/bbchen/bbchen.github.io.git"

def clean():
    if os.path.isdir(DEPLOY_PATH):
        local('rm -rf {deploy_path}'.format(**env))
        local('mkdir {deploy_path}'.format(**env))

def build():
    local('hugo')

def rebuild():
    clean()
    build()

def serve():
    local('hugo server')

def reserve():
    build()
    serve()

def github():
    # github_source()
    build()
    local('ghp-import -m "website updated" {deploy_path} && '
          'git push {github_address} gh-pages:master --force'.format(**env))

def github_source():
    local('git add --all && '
          'git commit -m "source updated" && '
          'git push origin source'.format(**env))

def publish():
    github_source()
    github()