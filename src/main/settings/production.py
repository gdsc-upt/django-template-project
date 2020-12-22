from .base import *

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

SILENCED_SYSTEM_CHECKS = [
    'security.W004',  # SECURE_HSTS_SECONDS
    'security.W008',  # SECURE_SSL_REDIRECT
]

if not DEBUG:
    SWAGGER_SETTINGS = {
        'USE_SESSION_AUTH': False,
        'VALIDATOR_URL': None,
    }
