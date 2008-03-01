#
# Default settings for Cheeserater project.
# The easiest way to use this is to make a settings.py file containting
# "from settings_template import *" and then override anything you need.
#

import os
_base = os.path.dirname(__file__)

TEMPLATE_DEBUG = DEBUG = True

# Database connection info
DATABASE_ENGINE = 'sqlite3'   
DATABASE_NAME = os.path.join(_base, 'cheeserater.db')
DATABASE_USER = ''     # Not used for sqlite
DATABASE_PASSWORD = '' # Not used for sqlite
DATABASE_HOST = ''     # Not used for sqlite
DATABASE_PORT = ''     # Not used for sqlite
                       
# Local time zone for this installation. All choices can be found here:
# http://www.postgresql.org/docs/8.1/static/datetime-keywords.html#DATETIME-TIMEZONE-SET-TABLE
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.w3.org/TR/REC-html40/struct/dirlang.html#langcodes
# http://blogs.law.harvard.edu/tech/stories/storyReader$15
LANGUAGE_CODE = 'en-us'

# Site ID in the Sites table
SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = False

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT.
# Example: "http://media.lawrence.com"
MEDIA_URL = ''

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = '0mlb6k(6087g@ixus_66li5v)!w18u=xtj!(fj5pjggx%n(zi^'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.doc.XViewMiddleware',
)

ROOT_URLCONF = 'cheeserater.urls'

TEMPLATE_DIRS = (
    os.path.join(_base, "templates"),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.humanize',
    'django.contrib.markup',
    'cheeserater.packages',
    'cheeserater.accounts',
    'cheeserater.votes',
)
