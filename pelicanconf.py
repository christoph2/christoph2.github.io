#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Christoph Schueler'
SITENAME = 'ASAM Intergration Package Newsfeed'

SITEURL = 'christoph2.github.io'
#SITESUBTITLE = 'Site Subtitle'
SITEDESCRIPTION = "Foo Bar's Thoughts and Writings"
#SITELOGO = SITEURL + "/images/profile.png"
#FAVICON = SITEURL + "/images/favicon.ico"


BROWSER_COLOR = "#333"
ROBOTS = "index, follow"

OUTPUT_PATH = '/'

PATH = 'content'
TIMEZONE = 'Europe/Berlin'
DEFAULT_LANG = 'en'
DEFAULT_DATE = "fs"

COPYRIGHT_YEAR = 2021

#EXTRA_PATH_METADATA = {
#    "extra/custom.css": {"path": "static/custom.css"},
#}

#CUSTOM_CSS = "static/custom.css"
MAIN_MENU = True



# Feed generation is usually not desired when developing
FEED_DOMAIN = SITEURL
FEED_ALL_ATOM = ''
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
FEED_RSS = "feeds/christoph2.rss"

# Blogroll
LINKS = (
    #('Pelican', 'https://getpelican.com/'),
    #('Python.org', 'https://www.python.org/'),
    #('Jinja2', 'https://palletsprojects.com/p/jinja/'),
    #('You can modify those links in your config file', '#'),
)

# Social widget
SOCIAL = (
    ('github', 'https://github.com/christoph2'),
#    ('You can add links in _your config file', '#'),
#    ('Another social link', '#'),
)

DEFAULT_CATEGORY = "open_source"

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

FILENAME_METADATA = '(?P<title>. * )'
LOAD_CONTENT_CACHE = False
SUMMARY_MAX_LENGTH = 60
DEFAULT_PAGINATION = 10
GITHUB_URL = 'https://github.com/christoph2'

THEME = 'themes/pelican-semantic-ui'

DISQUS_SITENAME = 'christoph2.github.io'
# GOOGLE_ANALYTICS = ''

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

#TYPOGRIFY = True
#TYPOGRIFY_DASHES = 'oldschool'

