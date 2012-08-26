# Django settings
import os, sys
import os.path
#gettext = lambda s: s
import djcelery
djcelery.setup_loader()


# Write here the project name
PROJECT_NAME = "sample_project"

# Get absolute project's path
PROJECT_PATH = os.path.abspath(os.path.split(__file__)[0])

# Theses settings are different with env variables
#
# We wait a DJANGO_MODE environment variable with values :
# 'production' OR 'development'
# See README
#
DJANGO_MODE = os.environ.get('DJANGO_MODE', False)
PRODUCTION_MODE = ( DJANGO_MODE == 'production' )
DEVELOPMENT_MODE = ( DJANGO_MODE == 'development' )
LOCAL_MODE = not ( PRODUCTION_MODE or DEVELOPMENT_MODE )

SYSPATH = sys.path

#################################
# Hosting configuration section #
#################################

ADMINS = (
     #('Jerome "jbl2024" Blondon', 'jerome@blondon.fr'),
)

SERVER_EMAIL = "%s@localhost" % PROJECT_NAME
DEFAULT_FROM_EMAIL = "%s@localhost" % PROJECT_NAME

BROKER_URL = "django://"
BROKER_BACKEND = "django"
CELERY_RESULT_BACKEND = "database"
CELERY_RESULT_DBURI = "sqlite:///db.dat"
CELERY_TASK_RESULT_EXPIRES = 10


# Some parameters can change between dev mode and prod mode
if PRODUCTION_MODE :
    DEBUG = False
    COMPRESS = True
    CACHE_BACKEND = 'memcached://127.0.0.1:11211/'
else :
    # DEVELOPMENT and LOCAL
    DEBUG = True
    COMPRESS = False

DATABASES = {}

if not LOCAL_MODE:
    # DEVELOPMENT and PRODUCTION
    DATABASES['default'] = { 
        'ENGINE': 'django.db.backends.mysql',
        'NAME': PROJECT_NAME,
        'OPTIONS': {'read_default_file': '~/.my.cnf',},
        }   
else :
    # In local mode use localdb
    DATABASES['default'] = {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': "db.dat",
        }

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
# We append PROJECT_PATH's absolute path
MEDIA_ROOT = os.path.join(PROJECT_PATH, 'media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/media/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/statics/admin/'

STATIC_URL = '/media/statics/'
STATIC_ROOT = os.path.join(MEDIA_ROOT, 'statics')

###############################################################################
# Dev section

TEMPLATE_DEBUG = DEBUG

MANAGERS = ADMINS

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/Paris'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en'
if PRODUCTION_MODE :
    LANGUAGE_CODE = 'fr'

TEST_LANGUAGE_CODE = 'en'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True
USE_L10N = True

# Make this unique, and don't share it with anybody.
SECRET_KEY = ''

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
    #'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.doc.XViewMiddleware',
    #'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    #'debug_toolbar.middleware.DebugToolbarMiddleware',
    #'django.middleware.cache.FetchFromCacheMiddleware',
)

ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_PATH, 'templates'),
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.request",
    #"messages.context_processors.inbox",
)

INTERNAL_IPS = (
    "127.0.0.1",
    )

SITE_NAME = "sample_project.com"
#LOGIN_URL = "/login/"
#LOGIN_REDIRECT_URLNAME = "registers"


LANGUAGES = (
    ('fr', 'French'),
    ('en', 'English'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.comments',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.markup',
    'django.contrib.staticfiles',

    # Contrib
    'djcelery',
    'kombu.transport.django',
    # Local
    'sample',
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(name)s:%(lineno)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'null': {
            'level':'DEBUG',
            'class':'django.utils.log.NullHandler',
        },
        'console':{
            'level':'DEBUG',
            'class':'logging.StreamHandler',
            'formatter': 'simple'
        },
        'debugfile':{
            'level':'DEBUG',
            'class':'logging.FileHandler',
            'filename': os.path.join(PROJECT_PATH, 'log/debug.log'),
            'formatter': 'verbose'
        },
        'file':{
            'level':'ERROR',
            'class':'logging.FileHandler',
            'filename': os.path.join(PROJECT_PATH, 'log/error.log'),
            'formatter': 'verbose'
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
        }
    },
    'loggers': {
        'django': {
            'handlers':['null'],
            'propagate': True,
            'level':'INFO',
        },
        'django.request': {
            'handlers': ['mail_admins', 'file'],
            'level': 'ERROR',
            'propagate': False,
        },
        'sample_project': {
            'handlers': ['console', 'file'],
            'level': 'ERROR',
        },
        'sample_project.dummy': {
            'handlers': ['console', 'file', 'debugfile'],
            'level': 'DEBUG',
            'propagate': False,
        },
    }
}

try:
    from local_settings import *
except ImportError:
    pass
