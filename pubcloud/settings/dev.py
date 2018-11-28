# encoding: utf-8
from .base import *  # NOQA

# DEBUG CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = True

# TOOLBAR CONFIGURATION
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

#INSTALLED_APPS += ('debug_toolbar',)

#MIDDLEWARE += ('debug_toolbar.middleware.DebugToolbarMiddleware',)
#INTERNAL_IPS = '127.0.0.1'

# EMAIL CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
