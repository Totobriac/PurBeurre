from . import *
import os

SECRET_KEY = os.environ.get('SK')
DEBUG = False
ALLOWED_HOSTS = ['188.166.26.54']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME'), 
        'USER': os.environ.get('DB_USER'), 
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': '',
        'PORT': '5432',
    }
}

