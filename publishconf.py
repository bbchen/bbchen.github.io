# Extend pelicanconf.py and apply some additional settings
import os, sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'http://bbchen.github.io'
RELATIVE_URLS = False
OUTPUT_PATH = 'deploy/'
