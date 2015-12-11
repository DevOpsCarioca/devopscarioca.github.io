#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'DevOpsCarioca'
SITENAME = 'DevOpsCarioca'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Sao_Paulo'

DEFAULT_LANG = 'br'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ('Pelican', 'http://getpelican.com/'),
    ('Python.org', 'http://python.org/'),
    ('Jinja2', 'http://jinja.pocoo.org/'),
    ('You can modify those links in your config file', '#'),
)

# Social widget
SOCIAL = (
    ('You can add links in your config file', '#'),
    ('Another social link', '#'),
)

DEFAULT_PAGINATION = 10

# Extras
STATIC_PATHS = [
    'images',
    # 'extras/CNAME',
    'extras/robots.txt',
    'extras/README',
]

EXTRA_PATH_METADATA = {
    # 'extras/CNAME': {'path': 'CNAME'},
    'extras/robots.txt': {'path': 'robots.txt'},
    'extras/README': {'path': 'README'}
}


RELATIVE_URLS = True
