from fabric.api import *
import fabric.contrib.project as project
import os
import sys
#import SimpleHTTPServer
#import SocketServer
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

# Remote server configuration
# production = 'binchen@imina.soest.hawaii.edu:22'
#dest_path = '/httpd/htdocs/HIGP/Faculty/binchen'

# # Rackspace Cloud Files configuration settings
# env.cloudfiles_username = 'my_rackspace_username'
# env.cloudfiles_api_key = 'my_rackspace_api_key'
# env.cloudfiles_container = 'my_cloudfiles_container'
# dest_path = '/httpd/htdocs/HIGP/Faculty/binchen'

# Rackspace Cloud Files configuration settings
# env.cloudfiles_username = 'my_rackspace_username'
# env.cloudfiles_api_key = 'my_rackspace_api_key'
# env.cloudfiles_container = 'my_cloudfiles_container'
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

# def cf_upload():
#     rebuild()
#     local('cd {deploy_path} && '
#           'swift -v -A https://auth.api.rackspacecloud.com/v1.0 '
#           '-U {cloudfiles_username} '
#           '-K {cloudfiles_api_key} '
#           'upload -c {cloudfiles_container} .'.format(**env))


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
    local('hugo -v')
    project.rsync_project(
        remote_dir=dest_path,
        exclude=".DS_Store",
        local_dir=DEPLOY_PATH.rstrip('/') + '/',
        delete=True,
        extra_opts='-c',
    )
