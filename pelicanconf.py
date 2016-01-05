<<<<<<< HEAD
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
=======
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
>>>>>>> master
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

<<<<<<< HEAD
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

=======
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

# DISQUS_SITENAME = 'zen-life'
>>>>>>> master
