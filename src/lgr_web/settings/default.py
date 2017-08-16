"""
Django settings for lgr_web project.

Generated by 'django-admin startproject' using Django 1.8.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from kombu import Exchange, Queue
from django.utils.translation import ugettext_lazy as _


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'PLEASE GENERATE ONE'

DEBUG = False

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = (
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'kombu.transport.django',
    'lgr_editor',
    'lgr_validator',
    'lgr_tools',
    'lgr_renderer',
    'widget_tweaks',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'lgr_web.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'lgr_web.wsgi.application'

# See http://docs.djangoproject.com/en/dev/topics/logging and
# http://docs.python.org/2/library/logging.config.html#configuration-dictionary-schema
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'default': {
            'format': '%(asctime)s %(levelname)s %(name)s [%(funcName)s:%(lineno)d] %(message)s'
        },
        'simple': {
            'format': '%(levelname)s [%(funcName)s:%(lineno)d] %(message)s'
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'console_rule_logger': {
            'level': 'ERROR',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'lgr_web': {
            'handlers': ['console'],
            'level': 'INFO',
        },
        'lgr_editor': {
            'handlers': ['console'],
            'level': 'INFO',
        },
        'lgr_tools': {
            'handlers': ['console'],
            'level': 'INFO',
        },
        'lgr': {
             'handlers': ['console'],
             'level': 'ERROR',
         },
        'lgr-rule-logger': {
            'handlers': ['console_rule_logger'],
            'level': 'INFO' # Need to be set to INFO!
        }
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/
LANGUAGE_CODE = 'en-us'
USE_I18N = True
USE_L10N = True

# where the non-app gettext translation catalogues can be found
LOCALE_PATHS = (
    os.path.abspath(os.path.join(BASE_DIR, 'locale')),
)

LANGUAGES = (
    ('ar', _('Arabic')),
    ('en', _('English')),
    ('fr', _('French')),
)

TIME_ZONE = 'UTC'
USE_TZ = True

# Session
# https://docs.djangoproject.com/en/1.8/topics/http/sessions/
SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_SECURE = True    # Secure setting - turn off for development
CSRF_COOKIE_HTTPONLY = False  # CSRF cookie is used by some JS for reference editing
CSRF_COOKIE_SECURE = True  # Secure setting for CSRF cookie - turn off for development

# How long to set the Session cookie for
SESSION_COOKIE_AGE = 60*60*24*14  # 2 weeks

# Where to store session data - use the database ("django.contrib.sessions.backends.db") for now
SESSION_ENGINE = 'django.contrib.sessions.backends.db'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    # Don't forget to use absolute paths, not relative paths.
    os.path.abspath(os.path.join(BASE_DIR, 'assets')),
)

##### LGR Toolset Project-specific settings #####
# Where the XML files are stored on the filesystem
# For the repertoires
REPERTOIRE_STORAGE_LOCATION = os.path.join(BASE_DIR, 'resources', 'repertoires')

# For the built-in LGRs
LGR_STORAGE_LOCATION = os.path.join(BASE_DIR, 'resources', 'lgr')

# Filepath of the LGR RNG schema file
LGR_RNG_FILE = os.path.join(BASE_DIR, 'resources', 'lgr.rng')

# For the tools output
TOOLS_OUTPUT_STORAGE_LOCATION = os.path.join(BASE_DIR, 'output')

# Duration in second for which the tools output files are stored
STORAGE_DURATION = 60*60*24*7  # 1 week

# Default variant type when creating new variant
DEFAULT_VARIANT_TYPE = "blocked"

SUPPORTED_UNICODE_VERSIONS = (
    '6.3.0',
)

# UNICODE_DATABASES tells munidata how to instantiate the implementation of each Unicode version that we support.
# Keys are the Unicode version, like '6.3.0'
# Values are a dict of the kwargs to pass to the munidata.manager.register function along with the version.
# Currently, we assume that the underlying implementation is "picu", so the value should have the following keys:
# - icu_uc_lib: full path to the libicuuc.so file
# - icu_i18n_lib': full path to the libicui18n.so file
# - version_tag: version tag used in the function symbols in the above libraries (usually the ICU major version)
# See picu.loader.KNOWN_ICU_VERSIONS

UNICODE_DATABASES = {
    '6.3.0': {
        'icu_uc_lib': '/usr/local/lib/libicuuc.so.52.1',
        'icu_i18n_lib': '/usr/local/lib/libicui18n.so.52.1',
        'version_tag': 52,
    },
}


# The following LGR_*_FUNC parameters decouple the lgr_validator module from the lgr_editor module
LGR_SELECTOR_FUNC = 'lgr_editor.api.session_select_lgr'
LGR_LIST_FUNC = 'lgr_editor.api.session_list_lgr'
UNIDB_LOADER_FUNC = 'lgr_editor.unidb.get_db_by_version'

# Validator will display variants inline if there are no more than the specified number of variants
# Otherwise, only a .csv download link is offered.
LGR_VALIDATOR_MAX_VARS_DISPLAY_INLINE = 100


##### /LGR Toolset Project-specific settings #####


##### Celery configuration parameters #####

CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_ACCEPT_CONTENT = ['json']

CELERYD_HIJACK_ROOT_LOGGER = False

CELERYD_TASK_SOFT_TIME_LIMIT = 60*60*24  # 24h
CELERYD_TASK_TIME_LIMIT = 3600*25  # 25h

CELERY_QUEUES = (
    Queue('celery', routing_key='transient',
          delivery_mode=1),
)

BROKER_URL = 'django://'

##### /Celery configuration parameters #####
