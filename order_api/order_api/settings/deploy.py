
# env 설정
import os
import environ

from .base import *


def read_secret(secret_name):
    file = open('/run/secrets/' + secret_name)
    secret = file.read()
    secret = secret.rstrip().lstrip()
    file.close()
    return secret


# 환경변수 불러올 수 있도록 세팅
env = environ.Env(DEBUG=(bool, True))


# env 파일의 위치 알려준다.
environ.Env.read_env(
    env_file=os.path.join(BASE_DIR, '.env')
)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = read_secret('DJANGO_SECRET_KEY')


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'yoonsu',
        'USER': 'yoonsu',
        'PASSWORD': read_secret('MYSQL_PASSWORD'),
        'HOST': 'mysql',
        'PORT': '3306',
    }
}