#!/usr/bin/env python

import codecs
import locale
import os
import re

from argh import *
from datetime import date, datetime
from fabric.api import local
from flask import Flask, render_template, abort
from flask_frozen import Freezer
from flaskext.flatpages import FlatPages
from flaskext.markdown import Markdown
from flaskext.assets import Environment as AssetManager
from PIL import Image, ImageOps
from shutil import copyfile
from unicodedata import normalize

# Configuration
DEBUG = False
BASE_URL = 'http://www.soest.hawaii.edu/HIGP/Faculty/binchen/'
ASSETS_DEBUG = DEBUG
FLATPAGES_AUTO_RELOAD = True
FLATPAGES_EXTENSION = '.md'
FLATPAGES_ROOT = 'contents'

# App configuration
FEED_MAX_LINKS = 25
SECTION_MAX_LINKS = 12

app = Flask(__name__)
app.config.from_object(__name__)
app.config['FREEZER_BASE_URL'] = BASE_URL
pages = FlatPages(app)
freezer = Freezer(app)
markdown_manager = Markdown(app, extensions=['fenced_code'], output_format='html5',)
asset_manager = AssetManager(app)


###############################################################################
# Model helpers

def get_pages(pages, offset=None, limit=None, section=None, year=None):
    """ Retrieves pages matching passec criterias.
    """
    articles = list(pages)
    # assign section value if none was provided in the metas
    for article in articles:
        if not article.meta.get('section'):
            article.meta['section'] = article.path.split('/')[0]
    # filter unpublished article
    if not app.debug:
        articles = [p for p in articles if p.meta.get('published') is True]
    # filter section
    if section:
        articles = [p for p in articles if p.meta.get('section') == section]
    # filter year
    if year:
        articles = [p for p in articles if p.meta.get('date').year == year]
    # sort by date
    articles = sorted(articles, reverse=True, key=lambda p: p.meta.get('date',
        date.today()))
    # assign prev/next page in serie
    for i, article in enumerate(articles):
        if i != 0:
            if section and articles[i - 1].meta.get('section') == section:
                article.prev = articles[i - 1]
        if i != len(articles) - 1:
            if section and articles[i + 1].meta.get('section') == section:
                article.next = articles[i + 1]
    # offset and limit
    if offset and limit:
        return articles[offset:limit]
    elif limit:
        return articles[:limit]
    elif offset:
        return articles[offset:]
    else:
        return articles


def get_years(pages):
    years = list(set([page.meta.get('date').year for page in pages]))
    years.reverse()
    return years


def resize_image(path, box, out=None, fit=True, quality=75):
    """ Downsample an image.

        @param path:    string - path to the original image
        @param box:     tuple(x, y) - the bounding box of the result image
        @param out:     file-like-object - save the image into the output stream
        @param fit:     boolean - crop the image to fill the box
        @param quality: int - JPEG quality
    """
    img = Image.open(path)
    if fit:
        img = ImageOps.fit(img, box, Image.ANTIALIAS)
    else:
        img.thumbnail(box, Image.ANTIALIAS)
    if not out:
        out = os.path.splitext(path)[0] + ".tn.jpg"
    img.save(out, "JPEG", quality=quality)


def section_exists(section):
    return not len(get_pages(pages, section=section)) == 0


def slugify(text, delim=u'-'):
    """Generates an slightly worse ASCII-only slug."""
    _punct_re = re.compile(r'[\t !"#$%&\'()*\-/<=>?@\[\\\]^_`{|},.]+')
    result = []
    for word in _punct_re.split(text.lower()):
        word = normalize('NFKD', word).encode('ascii', 'ignore')
        if word:
            result.append(word)
    return unicode(delim.join(result))


###############################################################################
# Filters

@app.template_filter()
def to_rfc2822(dt):
    if not dt:
        return
    current_locale = locale.getlocale(locale.LC_TIME)
    locale.setlocale(locale.LC_TIME, "en_US")
    formatted = dt.strftime("%a, %d %b %Y %H:%M:%S +0000")
    locale.setlocale(locale.LC_TIME, current_locale)
    return formatted


###############################################################################
# Context processors

@app.context_processor
def inject_ga():
    return dict(BASE_URL=BASE_URL)


###############################################################################
# Routes

@app.route('/contact/')
def contact():
    return render_template('contact.html')


@app.route('/feed/')
def feed():
    articles = get_pages(pages, limit=FEED_MAX_LINKS)
    now = datetime.now()
    return render_template('base.rss', pages=articles, build_date=now)


@app.route('/sitemap.xml')
def sitemap():
    today = date.today()
    recently = date(year=today.year, month=today.month, day=1)
    return render_template('sitemap.xml', pages=get_pages(pages),
        today=today, recently=recently)


@app.route('/<string:section>/feed/')
def feed_section(section):
    articles = get_pages(pages, limit=FEED_MAX_LINKS, section=section)
    return render_template('%s/feed.rss' % section, pages=articles,
        build_date=datetime.now())


@app.route('/')
def index():
    return render_template('index.html',
        news_posts=get_pages(pages, limit=5, section="news"),
        photos=get_pages(pages, limit=8, section="gallery"),
        posts=get_pages(pages, limit=5, section="blog"),
        talks=get_pages(pages, limit=5, section="talks"))


@app.route('/<path:path>/')
def page(path):
    # compute current "section" from path
    section = path.split('/')[0]
    page = pages.get_or_404(path)
    # ensure an accurate "section" meta is available
    page.meta['section'] = page.meta.get('section', section)
    # allow preview of unpublished stuff in DEBUG mode
    if not app.debug and not page.meta.get('published', False):
        abort(404)
    template = page.meta.get('template', '%s/page.html' % section)
    return render_template(template, page=page, section=section)


@app.route('/<string:section>/')
def section(section):
    if not section_exists(section):
        abort(404)
    template = '%s/index.html' % section
    articles = get_pages(pages, limit=SECTION_MAX_LINKS, section=section)
    years = get_years(get_pages(pages, section=section))
    return render_template(template, pages=articles, years=years)


@app.route('/<string:section>/<int:year>/')
def section_archives_year(section, year):
    if not section_exists(section):
        abort(404)
    template = '%s/archives.html' % section
    years = get_years(get_pages(pages, section=section))
    articles = get_pages(pages, section=section, year=year)
    return render_template(template, pages=articles, years=years, year=year)


@app.route('/403.html')
def error403():
    return render_template('403.html')


@app.route('/404.html')
def error404():
    return render_template('404.html')


@app.route('/500.html')
def error500():
    return render_template('500.html')


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


###############################################################################
# Commands

@command
def build():
    """ Builds this site.
    """
    print("Building website...")
    app.debug = False
    asset_manager.config['ASSETS_DEBUG'] = False
    freezer.freeze()
    local("cp ./static/*.ico ./build/")
    local("cp ./static/*.txt ./build/")
    local("cp ./static/*.xml ./build/")
    print("Done.")


@command
def deploy():
    build()
    local("rsync -avz -e ssh --exclude-from=rsync_exclude.txt "
          "./build/ imina.soest.hawaii.edu:/httpd/htdocs/HIGP/Faculty/binchen")


@command
def post(section, title=None, filename=None):
    """ Create a new empty post.
    """
    if not os.path.exists(os.path.join(FLATPAGES_ROOT, section)):
        raise CommandError(u"Section '%s' does not exist" % section)
    post_date = datetime.today()
    title = unicode(title) if title else "Untitled Post"
    if not filename:
        filename = u"%s.md" % slugify(title)
    year = post_date.year
    pathargs = [section, str(year), filename, ]
    filepath = os.path.join(os.path.abspath(os.path.dirname(__file__)),
        FLATPAGES_ROOT, '/'.join(pathargs))
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


@command
def photo(path, slug, section="gallery"):
    """ Adds a new photo.
    """
    photo_date = datetime.today()
    # check slug
    slug = slugify(unicode(slug))
    if not isinstance(slug, basestring) or not slug.strip():
        raise CommandError("Invalid slug: " + slug)
    # check that the path is valid, is an image
    if not os.path.exists(path) or not os.path.isfile(path):
        raise CommandError("Invalid path: " + path)
    # create directory for images: %year/%slug
    photo_dir = os.path.join("static", section, str(photo_date.year),
        slug)
    if os.path.exists(photo_dir):
        raise CommandError("path %s already exists" % photo_dir)
    os.mkdir(photo_dir, 0755)
    print(u'Created %s' % photo_dir)
    # copy original image to original.jpg
    original_path = os.path.join(photo_dir, "original.jpg")
    copyfile(path, original_path)
    print(u'Copied original to %s' % original_path)
    # resize the image: main.jpg and thumb.jpg
    thumb_path = os.path.join(photo_dir, "thumb.jpg")
    resize_image(original_path, (280, 280), fit=True, out=thumb_path)
    print(u'Created %s' % thumb_path)
    main_path = os.path.join(photo_dir, "main.jpg")
    resize_image(original_path, (900, 900), fit=False, out=main_path)
    print(u'Created %s' % main_path)
    # post file
    filename = slug + FLATPAGES_EXTENSION
    pathargs = [section, str(photo_date.year), filename, ]
    filepath = os.path.join(os.path.abspath(os.path.dirname(__file__)),
        FLATPAGES_ROOT, '/'.join(pathargs))
    if os.path.exists(filepath):
        raise CommandError("File %s exists" % filepath)
    content = '\n'.join([
        u"title: ",
        u"date: %s" % photo_date.strftime("%Y-%m-%d"),
        u"type: photo",
        u"published: false\n\n\n",
    ])
    try:
        codecs.open(filepath, 'w', encoding='utf8').write(content)
        print(u'Created %s' % filepath)
        os.system("open " + filepath)
    except Exception, error:
        raise CommandError(error)
    print('All done.')


@command
def serve(server='127.0.0.1', port=5000, debug=DEBUG):
    """ Serves this site.
    """
    asset_manager.config['ASSETS_DEBUG'] = debug
    if debug:
        app.debug = True
    app.run(host=server, port=port, debug=debug)


if __name__ == '__main__':
    parser = ArghParser()
    parser.add_commands([build, deploy, photo, post, serve, ])
    parser.dispatch()
