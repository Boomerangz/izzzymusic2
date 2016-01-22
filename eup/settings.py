"""
Django settings for eup project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '9y($9e)bla6bj!oysl9kw&%sgu^x$x=8+0qra_#ms40*-wer#o'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'music',

    'djcelery',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

import djcelery
djcelery.setup_loader()

ROOT_URLCONF = 'eup.urls'

WSGI_APPLICATION = 'eup.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
            'NAME': 'izzzymusic',                      # Or path to database file if using sqlite3.
            # The following settings are not used with sqlite3:
            'USER': 'izzzy',
            'PASSWORD': 'ooFxfq111',
            'HOST': 'izzzymusic.cpez7q0oykol.us-west-2.rds.amazonaws.com',                      # Empty for localhost through domain sockets or           '127.0.0.1' for localhost through TCP.
            'PORT': '5432',                      # Set to empty string for default.
        }
    }

# Internationalization./
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

TEMPLATE_DIRS = (os.path.join(BASE_DIR,  'templates'),)


BOT_TOKEN = '176784464:AAERe2JaWKTgqi8W4UVKtTBQWjOeoGY4G6Y'
URL = "https://api.telegram.org/bot%s/" % BOT_TOKEN
MyURL = "https://izzzymusic.xyz/message/"
import requests
r = requests.get(URL + "setWebhook?url=%s" % MyURL)
if r.status_code != 200:
    print "Can't set hook: %s. Quit." % r.text
    exit(1)