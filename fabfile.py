from fabric.api import *
import fabric.contrib.project as project
import os
import sys
import SimpleHTTPServer
import SocketServer
import datetime
import re
import codecs
from datetime import date, datetime
from unicodedata import normalize
from argh import *


# Local path configuration (can be absolute or relative to fabfile)
<<<<<<< HEAD
env.deploy_path = 'output'
=======
env.deploy_path = 'deploy'
>>>>>>> master
env.content_path = 'content'
DEPLOY_PATH = env.deploy_path
CONTENT_PATH = env.content_path

# Remote server configuration
production = 'binchen@imina.soest.hawaii.edu:22'
<<<<<<< HEAD
dest_path = '/httpd/htdocs/HIGP/Faculty/binchen'

# Rackspace Cloud Files configuration settings
env.cloudfiles_username = 'my_rackspace_username'
env.cloudfiles_api_key = 'my_rackspace_api_key'
env.cloudfiles_container = 'my_cloudfiles_container'
=======
# dest_path = '/httpd/htdocs/HIGP/Faculty/binchen'

# Rackspace Cloud Files configuration settings
# env.cloudfiles_username = 'my_rackspace_username'
# env.cloudfiles_api_key = 'my_rackspace_api_key'
# env.cloudfiles_container = 'my_cloudfiles_container'
env.github_address = "https://github.io/bbchen/bbchen.github.io.git"
>>>>>>> master


def clean():
    if os.path.isdir(DEPLOY_PATH):
        local('rm -rf {deploy_path}'.format(**env))
        local('mkdir {deploy_path}'.format(**env))

def build():
    local('pelican -s pelicanconf.py')

def rebuild():
    clean()
    build()

def regenerate():
    local('pelican -r -s pelicanconf.py')

def serve():
    os.chdir(env.deploy_path)

    PORT = 8000
    class AddressReuseTCPServer(SocketServer.TCPServer):
        allow_reuse_address = True

    server = AddressReuseTCPServer(('', PORT), SimpleHTTPServer.SimpleHTTPRequestHandler)

    sys.stderr.write('Serving on port {0} ...\n'.format(PORT))
    server.serve_forever()

def reserve():
    build()
    serve()

def preview():
    local('pelican -s publishconf.py')

def cf_upload():
    rebuild()
    local('cd {deploy_path} && '
          'swift -v -A https://auth.api.rackspacecloud.com/v1.0 '
          '-U {cloudfiles_username} '
          '-K {cloudfiles_api_key} '
          'upload -c {cloudfiles_container} .'.format(**env))

def post(section, title=None, filename=None):
    """ Create a new empty post.
    """
    if not os.path.exists(os.path.join(CONTENT_PATH, section)):
        raise CommandError(u"Section '%s' does not exist" % section)
    post_date = datetime.today()
    title = unicode(title) if title else "Untitled Post"
    if not filename:
        filename = u"%s.md" % slugify(title)
    year = post_date.year
<<<<<<< HEAD
    pathargs = [section, str(year), filename, ]
=======
    month = post_date.month
    day = post_date.day
    pathargs = [section, str(year), str(month) + "-" +  str(day) + " " + filename, ]
>>>>>>> master
    filepath = os.path.join(os.path.abspath(os.path.dirname(__file__)),
        CONTENT_PATH, '/'.join(pathargs))
    if os.path.exists(filepath):
        os.system("open " + filepath)
        raise CommandError("File %s exists" % filepath)
    content = '\n'.join([
        u"title: %s" % title,
        u"date: %s" % post_date.strftime("%Y-%m-%d"),
        u"published: false\n\n",
    ])
    try:
        codecs.open(filepath, 'w', encoding='utf8').write(content)
        print(u'Created %s' % filepath)
<<<<<<< HEAD
        os.system("open " + filepath)
=======
        # os.system("open " + filepath)
>>>>>>> master
    except Exception, error:
        raise CommandError(error)

def page(section, title=None, filename=None):
    """ Create a new empty post.
    """
    if not os.path.exists(os.path.join(CONTENT_PATH, section)):
        raise CommandError(u"Section '%s' does not exist" % section)
    post_date = datetime.today()
    title = unicode(title) if title else "Untitled Post"
    if not filename:
        filename = u"%s.md" % slugify(title)
    year = post_date.year
    pathargs = [section, filename, ]
    filepath = os.path.join(os.path.abspath(os.path.dirname(__file__)),
        CONTENT_PATH, '/'.join(pathargs))
    if os.path.exists(filepath):
        os.system("open " + filepath)
        raise CommandError("File %s exists" % filepath)
    content = '\n'.join([
        u"title: %s" % title,
        u"date: %s" % post_date.strftime("%Y-%m-%d"),
        u"published: false\n\n",
    ])
    try:
        codecs.open(filepath, 'w', encoding='utf8').write(content)
        print(u'Created %s' % filepath)
        os.system("open " + filepath)
    except Exception, error:
        raise CommandError(error)

def slugify(text, delim=u'-'):
    """Generates an slightly worse ASCII-only slug."""
    _punct_re = re.compile(r'[\t !"#$%&\'()*\-/<=>?@\[\\\]^_`{|},.]+')
    result = []
    for word in _punct_re.split(text.lower()):
        word = normalize('NFKD', word).encode('ascii', 'ignore')
        if word:
            result.append(word)
    return unicode(delim.join(result))

<<<<<<< HEAD
=======
def github():
    build()
    local('ghp-import -m "website updated" {deploy_path} && '
          'git push {github_address} gh-pages:master --force'.format(**env))

>>>>>>> master
@hosts(production)
def publish():
    local('pelican -s publishconf.py')
    project.rsync_project(
        remote_dir=dest_path,
        exclude=".DS_Store",
        local_dir=DEPLOY_PATH.rstrip('/') + '/',
        delete=True,
        extra_opts='-c',
    )
