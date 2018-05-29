from .settings import *

ALLOWED_HOSTS += ['127.0.0.1', 'localhost']

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
