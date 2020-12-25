import logging

from main.settings.common import *

INSTALLED_APPS += [
    'debug_toolbar',
    'nplusone.ext.django',
]

MIDDLEWARE += [
    'nplusone.ext.django.NPlusOneMiddleware',
    'querycount.middleware.QueryCountMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

NPLUSONE_LOGGER = logging.getLogger('nplusone')
NPLUSONE_LOG_LEVEL = logging.WARN

LOGGING = {
    'version': 1,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'nplusone': {
            'handlers': ['console'],
            'level': 'WARN',
        },
    },
}

QUERYCOUNT = {
    'DISPLAY_DUPLICATES': 100,
}

INTERNAL_IPS = [
    '127.0.0.1',
]
