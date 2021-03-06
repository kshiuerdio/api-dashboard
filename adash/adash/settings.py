"""
Django settings for adash project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'pn#!$jqyyx(2_#ob@j2xccafpbbe*r(=5h0f#5jl*felqy2e+2'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

SETTINGS_PATH = os.path.normpath(os.path.dirname(__file__))
TEMPLATE_DIRS = (
  os.path.join(SETTINGS_PATH, '../adashboard/templates'),
)

STATICFILES_DIRS = (
  os.path.join(BASE_DIR, "static"),
  os.path.join(BASE_DIR, "adashboard/static"),
)

DATA_SOURCE_KEYS = {
  'twitter' : {
    'consumer_key' : os.environ.get('TWITTER_CONSUMER_KEY', None),
    'consumer_secret' : os.environ.get('TWITTER_CONSUMER_SECRET', None),
    'access_key' : os.environ.get('TWITTER_ACCESS_KEY', None),
    'access_secret' : os.environ.get('TWITTER_ACCESS_SECRET', None)
  }
}

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'adashboard',
    'south'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'adash.urls'

WSGI_APPLICATION = 'adash.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'adash',
        'USER': 'rdioapi',
        'PASSWORD': 'rdiorocks',
        'HOST': 'localhost'
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/adash.static-files/

STATIC_URL = '/static/'
