from .settings import *

ALLOWED_HOSTS += ['127.0.0.1', 'localhost']

EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = 'memberit'
EMAIL_HOST_PASSWORD = '..asdf1234'
EMAIL_PORT = 465
EMAIL_USE_SSL = True
