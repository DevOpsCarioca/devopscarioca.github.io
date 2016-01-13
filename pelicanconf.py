#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'DevOpsCarioca'
SITENAME = 'DevOpsCarioca'
SITEURL = 'http://www.devopscarioca.com.br'

GITHUB_URL = 'http://github.com/DevOpsCarioca'
TWITTER_URL = 'http://twitter.com/DevOpsCarioca'
FACEBOOK_URL = 'http://facebook.com/DevOpsCarioca'

PATH = 'content'

THEME = "theme"

TIMEZONE = 'America/Sao_Paulo'

DEFAULT_LANG = 'br'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Next meetup info
MEETUP_DATE_LABEL = "Próximo encontro: "
MEETUP_DATE = "a definir"
MEETUP_PLACE_LABEL = "Local: "
MEETUP_PLACE = "a definir"
MEETUP_ADDRESS_LABEL = "Endereço: "
MEETUP_ADDRESS = "a definir"

# Blogroll
LINKS = (
    ('Pelican', 'http://getpelican.com/'),
    ('Python.org', 'http://python.org/'),
    ('Jinja2', 'http://jinja.pocoo.org/'),
    ('You can modify those links in your config file', '#'),
)

# Social widget
SOCIAL = (
    ('MeetUp', 'http://www.meetup.com/pt/DevOps-Carioca/'),
    ('Facebook', 'https://www.facebook.com/DevOpsCarioca/'),
    ('Twitter', 'https://twitter.com/devopscarioca'),
)

DEFAULT_PAGINATION = 10

# Extras
STATIC_PATHS = [
    'images',
    'extras/CNAME',
    'extras/robots.txt',
    'extras/README',
    'extras/favicon.ico',
]

EXTRA_PATH_METADATA = {
    'extras/CNAME': {'path': 'CNAME'},
    'extras/robots.txt': {'path': 'robots.txt'},
    'extras/README': {'path': 'README'},
    'extras/favicon.ico': {'path': 'favicon.ico'}
}


RELATIVE_URLS = True
