import os.path

PROJECT_DIR = os.path.realpath(os.path.dirname(__file__))
BUILDOUT_DIR = os.path.abspath(os.path.join(PROJECT_DIR, '..', '..'))

MEDIA_ROOT = os.path.join(BUILDOUT_DIR, 'var', 'www', 'media')
STATIC_ROOT = os.path.join(BUILDOUT_DIR, 'var', 'www', 'static')
