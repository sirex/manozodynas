# coding: utf-8

from __future__ import unicode_literals

import os

from django.conf.global_settings import *  # noqa

from manozodynas.settings.apps import *  # noqa
from manozodynas.settings.paths import *  # noqa
from manozodynas.settings.logging import *  # noqa
from manozodynas.settings.testing import *  # noqa
from manozodynas.settings.security import *  # noqa

ADMINS = (
    ('Albertas', 'albertasgim@gmail.com'),
)
MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BUILDOUT_DIR, 'var', 'db'),
    }
}

SITE_ID = 1

LANGUAGE_CODE = 'lt'
LANGUAGES = (
    ('lt', gettext_noop('Lithuanian')),
    ('en', gettext_noop('English')),
)

USE_L10N = True

MEDIA_URL = '/media/'
STATIC_URL = '/static/'

ROOT_URLCONF = 'manozodynas.settings.urls'

AUTH_USER_MODEL = 'users.User'
LOGIN_URL = '/login/'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'manozodynas.lt'
EMAIL_HOST_USER = 'info@manozodynas.lt'
DEFAULT_FROM_EMAIL = 'info@manozodynas.lt'


TEMPLATE_LOADERS += (
    'django.template.loaders.eggs.Loader',
)
