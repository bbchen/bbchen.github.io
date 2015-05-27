#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Bin Chen'
SITENAME = u'Bin Chen, Mineral Physics Laboratory'
#SITEURL = 'http://www.soest.hawaii.edu/HIGP/Faculty/binchen'
SITEURL = ''

PATH = 'content'
THEME = 'themes/higp'
PLUGIN_PATHS = ['plugins']
PLUGINS = ['sitemap', 'tipue_search', 'render_math', 'pelican-bibtex']
PUBLICATIONS_SRC = 'content/publications/pubs.bib'

TIMEZONE = 'US/Pacific-New'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = None
"""(('Pelican', 'http://getpelican.com/'),
 ('Python.org', 'http://python.org/'),
 ('Jinja2', 'http://jinja.pocoo.org/'),
 ('You can modify those links in your config file', '#'),)
"""

# Social widget
SOCIAL = () 
"""(('You can add links in your config file', '#'),
('Another social link', '#'),) """

# Menu
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_TAGS_ON_MENU = False
DISPLAY_ARCHIVES_ON_MENU = False
# MENUITEMS = (
#         ('Publications', 'publications.html'),
#         ('News', 'news/')
#     )

# Templates
DIRECT_TEMPLATES = ('index', 'news','tags', 'categories', 'archives', 'search', '404')
PAGINATED_DIRECT_TEMPLATES = ('index',)
STATIC_PATHS = ['theme/images', 'images', 'CNAME']

PAGE_PATHS = ['pages','people','facilities']
ARTICLE_PATHS = ['news']

# URL
ARTICLE_URL = 'news/{date:%Y}/{date:%b}-{date:%d}-{slug}.html'
ARTICLE_SAVE_AS = 'news/{date:%Y}/{date:%b}-{date:%d}-{slug}.html'
ARTICLE_LANG_URL = 'news/{date:%Y}/{date:%b}-{date:%d}-{slug}.html'
ARTICLE_LANG_SAVE_AS = 'news/{date:%Y}/{date:%b}-{date:%d}-{slug}.html'
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'
PAGE_LANG_URL = '{slug}.html'
PAGE_LANG_SAVE_AS = '{slug}-{lang}.html'
CATEGORY_URL = 'news/category/{slug}.html'
CATEGORY_SAVE_AS = 'news/category/{slug}.html'
TAG_URL = 'news/tag/{slug}.html'
TAG_SAVE_AS = 'news/tag/{slug}.html'
NEWS_SAVE_AS = 'news/index.html'

DEFAULT_PAGINATION = 12

# Sitemap
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}

RELATIVE_URLS = True

# Theme specific
EMAIL_ADDRESSS = "binchen@hawaii.edu"
TWITTER_ADDRESS = "www.twitter.com/bbchen"
PROFILE_IMAGE_URL = "logo.png"
SITE_LICENSE = "Copyright &copy; 2014 Bin Chen"
SHOW_ARTICLE_AUTHOR = False

