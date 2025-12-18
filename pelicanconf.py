AUTHOR = 'DZ'
SITENAME = '瞎扯淡'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Asia/Singapore'

DEFAULT_LANG = 'zh_CN'
# DEFAULT_DATE_FORMAT = {
#     'en': '%a, %d %b %Y',
#     'zh': '%Y-%m-%d(%a)',
# }

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = None #(('Pelican', 'https://getpelican.com/'),
         # ('Python.org', 'https://www.python.org/'),
         # ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         # ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = None #(('You can add links in your config file', '#'),
         # ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
OUTPUT_PATH = "docs/"

# Plugin configuration: prefer installing plugins into the Python environment
# and listing them here by import name. Remove any hard-coded absolute
# filesystem paths so the project is portable.
# Load plugins from the bundled `pelican-plugins` directory (cloned locally).
PLUGIN_PATHS = ['plugins/cjk-auto-spacing', 'plugins']
PLUGINS = ['cjk_auto_spacing']
# Enable automatic spacing for CJK content
CJK_AUTO_SPACING = True

MARKDOWN = {
  'extensions': ['markdown.extensions.attr_list']
}
