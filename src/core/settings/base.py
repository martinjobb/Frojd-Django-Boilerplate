#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Django settings for Fröjd Django projects.
"""

import os

from core.settings import get_env, get_env_bool


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Version, be sure to bump this with each release (please follow semver.org)
APP_VERSION = '0.0.1'

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = get_env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = get_env_bool('DEBUG')

# Minified, by default it is set to the same as Debug
MINIFIED = get_env_bool('MINIFIED', default=not DEBUG)

# This is when debug is off, else django wont allow you to visit the site
ALLOWED_HOSTS = get_env('ALLOWED_HOSTS').split(',')

INTERNAL_IPS = (
    '127.0.0.1',
)


# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 'pages', # Uncomment this to activate the example app
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'
APPEND_SLASH = True

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            'templates',
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'debug': True,
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                # Project specific
                'core.context_processors.settings_context_processor',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases
# Using PostgreSQL
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': get_env('DATABASE_NAME'),
        'USER': get_env('DATABASE_USER'),
        'PASSWORD': get_env('DATABASE_PASSWORD'),
        'HOST': get_env('DATABASE_HOST'),
        'PORT': get_env('DATABASE_PORT'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',  # NOQA
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',  # NOQA
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',  # NOQA
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',  # NOQA
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/
LANGUAGE_CODE = 'sv-SE'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Uploaded media
MEDIA_URL = '/media/'
MEDIA_ROOT = get_env('MEDIA_PATH')


# Static files, if in production use static root, else use static dirs

# Static URL to use when referring to static files located in STATIC_ROOT.
STATIC_URL = '/static/'

# The absolute path to the directory where collectstatic will collect static
# files for deployment. Example: "/var/www/example.com/static/"I
STATIC_ROOT = get_env('STATIC_PATH')

# This setting defines the additional locations the staticfiles will traverse
STATICFILES_DIRS = (
    # "/home/special.polls.com/polls/static",
    # "/home/polls.com/polls/static",
)


# Example metadata
GA_ACCOUNT = get_env('GA_ACCOUNT', default="GA-XXXX")
