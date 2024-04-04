from .base import *
import os

DEBUG = True

print("AMBIENTE: PRODUÇÃO")

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/staticfiles/'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_ROOT2 = os.path.join(BASE_DIR, 'media', 'local')
STATICFILES_DIRS = [(os.path.join(BASE_DIR, 'statics'))]