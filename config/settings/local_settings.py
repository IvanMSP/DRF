from .base import *

DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'drf_api',
        'USER': 'valor_user',
        'PASSWORD': 'xHsd34.$',
        'HOST': 'localhost',
        'PORT': ''
       },
   }

STATIC_URL = '/static/'
