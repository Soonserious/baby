"""
Django settings for babysecurity project.

Generated by 'django-admin startproject' using Django 2.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os
import pymysql



# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

pymysql.install_as_MySQLdb()

dbSetupList = []
mediaSetupList =[]

with open(BASE_DIR+"\\setup\\db_setting.txt","r") as f:
    for line in f:
        dbSetupList.append(line.rstrip("\n"))
    f.close()

with open(BASE_DIR+"\\setup\\media_setting","r") as f:
    for line in f:
        mediaSetupList.append(line.rstrip("\n"))
    f.close()

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'n9uqz(@wpvk2x640(&4zfm5^#9xpp6-8yh51amt8i=@dayg2#3' #설정파일로 바꾸기

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]

MEDIA_URL = "/media/"
MEDIA_ROOT = mediaSetupList[0]
# Application definition
STATIC_URL = "/static/"
STATICFILES_DIRS = ("C:/Users/Administrator/Downloads/backyardHighConvertinglandingpage-bootstrap4/backyardHighConvertinglandingpage-bootstrap4/",)


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'account',
    'parent',
    'rasberrypy',
    'errorpage',
]

LOGGING = {
    'version': 1,
               'disable_existing_loggers': False,
    'formatters': {
            'format1': {
            'format': '[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s',
            'datefmt': '%d/%b/%Y %H:%M:%S'
        },
        'format2': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'logs/logfile'),
            'formatter': 'format1',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'format2',
        }
    },
    'loggers': {
        'account': {
            'handlers': ['file'],
            'level': 'DEBUG',
        },
        'parent': {
            'handlers': ['file'],
            'level': 'DEBUG',
        },
        'rasberrypy': {
            'handlers': ['file'],
            'level': 'DEBUG',
        },

         'django.request': {
             'handlers': ['file'],
             'level': 'DEBUG',  # change debug level as appropiate
             'propagate': False,

        },
    },
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'request_logging.middleware.LoggingMiddleware',
]

ROOT_URLCONF = 'babysecurity.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'babysecurity.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
'default': {
        'ENGINE': dbSetupList[0],
        'NAME': dbSetupList[1],
        "USER": dbSetupList[2],
        "PASSWORD" : dbSetupList[3],
        "HOST" : dbSetupList[4],
        "PORT" : dbSetupList[5],
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'validator.minimumvalidator.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

AUTH_USER_MODEL="account.User"

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'