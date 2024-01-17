AUTHOR = 'Steve'
SITENAME = "Steve's Website"
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# My Configs
MENUITEMS = [
    ("Home", "/index.html"),
    # ("Categories", "/categories.html"),
    # ("Tags", "/tags.html"),
    # ("Series", "/series.html"),
    ("Articles", "/archives.html"),
    ("About Me", "/about-me.html")
]

# might wind up needing to add 'images' to this
STATIC_PATHS = ['extra/favicon.ico']
DEFAULT_METADATA = {
    'status': 'draft',
}
EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'}
}

# THEME configs
THEME = 'theme'

# https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes
DEFAULT_DATE_FORMAT = ('%b %d, %Y %I:%M %p')

RECENT_POST_LIST_LENGTH = 5

TEMPLATE_PAGES = {
    'tables-of-contents.html': 'tables-of-contents.html',
    'series.html': 'series.html',
    'about-me.html': 'about-me.html'
}