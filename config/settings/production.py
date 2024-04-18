from .base import *

DEBUG = False

print("AMBIENTE: PRODUÇÃO")

# aws settings
AWS_ACCESS_KEY_ID = config("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = config("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = config("AWS_STORAGE_BUCKET_NAME")
AWS_DEFAULT_ACL = config("AWS_DEFAULT_ACL")
AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400'}

STATICFILES_DIRS = [(os.path.join(BASE_DIR, 'statics'))]

# s3 static settings
STATIC_LOCATION = 'static'
STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATIC_LOCATION}/'
STATICFILES_STORAGE = 'config.storage_backends.StaticStorage'

# s3 public media settings
PUBLIC_MEDIA_LOCATION = 'media'
MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{PUBLIC_MEDIA_LOCATION}/'
DEFAULT_FILE_STORAGE = 'config.storage_backends.PublicMediaStorage'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(asctime)s: %(levelname)s - %(name)s (%(module)s.py).  %(message)s',
        }
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'verbose',
            'filename': '/root/logs/crud-django/debug.log',
            'backupCount': 10,
            'maxBytes': 5242880,  # 5*1024*1024 bytes (5MB)
        },
    },
    'loggers': {
        'django.server': {
            'handlers': ['file'],
            'level': 'INFO',
        },
        'django.request': {
            'handlers': ['file'],
            'level': 'ERROR',
            'propagate': False,
        },
        'django.template': {
            'handlers': ['file'],
            'level': 'ERROR',
            'propagate': False,
        },
    },
}
