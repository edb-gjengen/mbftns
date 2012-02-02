from os.path import dirname, join

def map_path(target_name):
    '''Enables path names to be decided at runtime.'''
    return join(dirname(__file__), target_name).replace('\\', '/')

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': map_path('dev.db'),                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    },
    'radius': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'radius',                # Or path to database file if using sqlite3.
        'USER': 'radius',                # Not used with sqlite3.
        'PASSWORD': '',  # Not used with sqlite3.
        'HOST': 'localhost',             # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

DATABASE_ROUTERS = ['main.router.Router']

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/Oslo'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'no-nb'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = ''

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = ''

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# URL prefix for admin static files -- CSS, JavaScript and images.
# Make sure to use a trailing slash.
# Examples: "http://foo.com/static/admin/", "/static/admin/".
ADMIN_MEDIA_PREFIX = '/static/admin/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    map_path('static'),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'osv$uy-ea$*%lc)+xiwt5@2b7au%u*c!pa6hmh#vl)*+tp%fss'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    map_path('main/templates'),
)

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.humanize',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'main',
    'radius',
)
AUTHENTICATION_BACKENDS = (
    'django_auth_ldap.backend.LDAPBackend',
    'django.contrib.auth.backends.ModelBackend',
)
# No cleaningladies.
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
SESSION_COOKIE_AGE = 60 * 15 # in seconds

# LDAP server URI and BIND_DN, same as db-settings
AUTH_LDAP_SERVER_URI = 'ldap://pacman.neuf.no'
AUTH_LDAP_BIND_DN = 'uid=admin,ou=People,dc=neuf,dc=no'
AUTH_LDAP_BIND_PASSWORD = ''

import ldap
from django_auth_ldap.config import LDAPSearch, PosixGroupType

# Basic user auth
AUTH_LDAP_USER_SEARCH = LDAPSearch(
    "ou=People,dc=neuf,dc=no",
    ldap.SCOPE_ONELEVEL,
    "(uid=%(user)s)")
AUTH_LDAP_USER_DN_TEMPLATE = "uid=%(user)s,ou=People,dc=neuf,dc=no"
# Basic groups
AUTH_LDAP_GROUP_SEARCH = LDAPSearch(
    "ou=Groups,dc=neuf,dc=no",
    ldap.SCOPE_ONELEVEL,
    "(objectClass=posixGroup)")
AUTH_LDAP_GROUP_TYPE = PosixGroupType()
# Mirror groups on each auth
AUTH_LDAP_MIRROR_GROUPS = True
# Group to user flag mappings
AUTH_LDAP_USER_FLAGS_BY_GROUP = {
    "is_active": "cn=dns-alle,ou=Groups,dc=neuf,dc=no",
    "is_staff": "cn=edb,ou=Groups,dc=neuf,dc=no",
    "is_superuser": "cn=edbadmin,ou=Groups,dc=neuf,dc=no"
}
AUTH_LDAP_REQUIRE_GROUP = LDAPSearch(
    "ou=Groups,dc=neuf,dc=no",
    ldap.SCOPE_ONELEVEL,
    "(|(cn=dns-styret)(cn=dns-admin)(cn=dns-billettluka)(cn=edb))")
# Group to profile flag mappings, not used.
AUTH_LDAP_PROFILE_FLAGS_BY_GROUP = {
    #"is_edb": "cn=edb,ou=Groups,dc=neuf,dc=no"
}
# User attribute mappings
AUTH_LDAP_USER_ATTR_MAP = {
    "first_name": "givenName",
    "last_name": "sn",
    "email": "mail",
}
# User profile attribute mappings
AUTH_LDAP_PROFILE_ATTR_MAP = {
    "home_directory": "homeDirectory"
}
# Allways update the django user object on authentication.
AUTH_LDAP_ALWAYS_UPDATE_USER = True

# Debug logging
import logging
logger = logging.getLogger('django_auth_ldap')
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.DEBUG)


# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

LOGIN_REDIRECT_URL = '/system/'
