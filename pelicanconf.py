#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'The LLEMR Conspiracy'
SITENAME = 'The LLEMR Conspiracy'
SITEURL = 'https://llemrconspiracy.org'

PATH = 'content'

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = 'en'

THEME = 'themes/bootstrap'

STATIC_PATHS = ['images', 'keys']

GITHUB_ORG_URL = 'https://github.com/oslerproject'
GITHUB_PROJECT_URL = GITHUB_ORG_URL+'/llemr'
DOCS_URL = 'https://llemr.readthedocs.io/'
DEMO_URL = 'https://oslerdemo.herokuapp.com'

MENUITEMS = {
    'left': [
        ('Home', '/'),
        ('Blog', '/blog/'),
        ('About','/authors'),
    ],
    'right' : [
        ('Demo', DEMO_URL),
        ('Docs', DOCS_URL),
        ('Source', GITHUB_PROJECT_URL),
    ]
}

# move all the articles to a subfolder called 'blog'
ARTICLE_URL = 'blog/{slug}/'
ARTICLE_SAVE_AS = 'blog/{slug}/index.html'
ARCHIVES_SAVE_AS = 'blog/index.html'

ARTICLE_ORDER_BY = 'date'

# The URL to refer to an article draft.
DRAFT_URL = 'blog/drafts/{slug}/'
DRAFT_SAVE_AS = 'blog/drafts/{slug}/index.html'

# Feed generation is usually not desired when developing
FEED_ALL_RSS = 'blog/feeds/all.rss.xml'
FEED_ALL_ATOM = 'blog/feeds/all.atom.xml'
FEED_MAX_ITEMS = 15

FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DIRECT_TEMPLATES = ['index', 'authors', 'archives']
DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
