#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

DEFAULT_LANG = u'en'

# Theme-specific settings
SITENAME = 'Zen Life'
DOMAIN = 'bbchen.github.io'
SITEURL = 'http://bbchen.github.io'
BIO_TEXT = 'Earth Science, Zen Life'
FOOTER_TEXT = 'Powered by <a href="http://getpelican.com">Pelican</a> and <a href="http://pages.github.com">GitHub&nbsp;Pages</a>.'

SITE_AUTHOR = 'bbchen'
TWITTER_USERNAME = '@bbchen'
GOOGLE_PLUS_URL = 'https://plus.google.com/+bbchen'
INDEX_DESCRIPTION = 'Website and blog of bbchen, an Earth scientist from Honolulu, HI, USA'

SIDEBAR_LINKS = [
    '<a href="/about/">About</a>',
    '<a href="/archive/">Archive</a>',
]

# Paths
PATH = 'content'
OUTPUT_PATH = 'deploy'
ICONS_PATH = 'images/icons'
PAGE_PATHS = ['pages']
ARTICLE_PATHS = ['posts']
STATIC_PATHS = ['images', 'extra']

IGNORE_FILES = ['.DS_Store', 'pneumatic.scss', 'pygments.css']

GOOGLE_FONTS = [
    "Raleway:400,600",
    "Source Code Pro",
]

SOCIAL_ICONS = [
    ('mailto:bbchen@gmail.com', 'Email (bbchen@gmail.com)', 'fa-envelope'),
    ('http://twitter.com/bbchen', 'Twitter', 'fa-twitter'),
    ('http://github.com/bbchen', 'GitHub', 'fa-github'),
]

# Theme configuration
THEME_COLOR = '#FF8000'
THEME = 'themes/pneumatic'

# Pelican settings
RELATIVE_URLS = True
TIMEZONE = 'US/Pacific-New'
DEFAULT_DATE = 'fs'
DEFAULT_DATE_FORMAT = '%B %d, %Y'
DEFAULT_PAGINATION = False
SUMMARY_MAX_LENGTH = 42

ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}/'
ARTICLE_SAVE_AS = ARTICLE_URL + 'index.html'

PAGE_URL = '{slug}/'
PAGE_SAVE_AS = PAGE_URL + 'index.html'

ARCHIVES_SAVE_AS = 'archive/index.html'
YEAR_ARCHIVE_SAVE_AS = '{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = '{date:%Y}/{date:%m}/index.html'

# Disable authors, categories, tags, and category pages
DIRECT_TEMPLATES = ['index', 'archives']
CATEGORY_SAVE_AS = ''

# Disable Atom feed generation
FEED_ATOM = 'atom.xml'
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

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
DIRECT_TEMPLATES = ('index', 'tags', 'categories', 'archives')
PAGINATED_DIRECT_TEMPLATES = ('index',)
STATIC_PATHS = ['theme/images', 'images', 'CNAME']

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

TYPOGRIFY = True
MD_EXTENSIONS = ['admonition', 'codehilite(linenums=True)', 'extra']

CACHE_CONTENT = False
DELETE_OUTPUT_DIRECTORY = True

templates = ['404.html']
TEMPLATE_PAGES = {page: page for page in templates}

extras = ['CNAME', 'favicon.ico', 'keybase.txt', 'robots.txt']
EXTRA_PATH_METADATA = {'extra/%s' % file: {'path': file} for file in extras}

# Plugins
PLUGIN_PATHS = ['plugins']
PLUGINS = ['assets', 'neighbors', 'render_math']
ASSET_SOURCE_PATHS = ['static']
ASSET_CONFIG = [
   ('cache', False),
   ('manifest', False),
   ('url_expire', False),
   ('versions', False),
]

DISQUS_SITENAME = 'zen-life'
