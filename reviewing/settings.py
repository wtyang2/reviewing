"""
Django settings for miniprogram project.

Generated by 'django-admin startproject' using Django 1.11.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""


import os
import datetime
import decimal
import sys  # 4
reload(sys)
sys.setdefaultencoding('utf-8')


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '6l96=e*-y!^4w+3dg&*liclqe!2tc_c$w2f#x)*(&p_m7&aao9'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

USE_MYSQL = False

# TODO: Add host name
ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'corsheaders',
    'simple_history',

    'base.apps.BaseConfig',
    'usersys.apps.UsersysConfig',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'base.middleware.session.WLSessionMiddleware',

    'corsheaders.middleware.CorsMiddleware',
    'simple_history.middleware.HistoryRequestMiddleware',

    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'base.middleware.adp.AntiDuplicatePostMiddleware',
]

ROOT_URLCONF = 'reviewing.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'reviewing.wsgi.application'


# DRF

REST_FRAMEWORK = {
    'DATETIME_FORMAT': '%s',
}


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

# Change database
if USE_MYSQL:
    SILENCED_SYSTEM_CHECKS = ['mysql.E001']
    DATABASES = {
        'default': {
            'ENGINE': 'base.db.mysql_enhanced',
            'OPTIONS': {
                'read_default_file': os.path.join(BASE_DIR, 'client')
            },
        }
    }

else:

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# User model

AUTH_USER_MODEL = 'usersys.UserBase'

# Add LOG
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'formatters': {
        'stream': {
            'format': '%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
        },
        'debug_stream': {
            'format': '%(asctime)s %(name)-12s %(levelname)-8s %(pathname)s'
                      ' %(lineno)d %(message)s',
        },
        'request_stream': {
            '()': 'base.util.log.RequestDetailFormatter',
            'format':  '%(asctime)s %(name)-12s %(levelname)-8s'
                       ' %(request_method)s %(request_uri)s %(request_body)s'
                       ' %(message)s',
        },
    },
    'handlers': {
        'stream': {
            'class': 'logging.StreamHandler',
            'formatter': 'stream',
        },
        'debug_stream': {
            'class': 'logging.StreamHandler',
            'formatter': 'debug_stream',
            'filters': ['require_debug_true'],
        },
        'request_stream': {
            'class': 'logging.StreamHandler',
            'formatter': 'request_stream',
        },
    },
    'loggers': {
        'django.db.backends': {
            'handlers': ['debug_stream'],
            'level': 'INFO',
        },
        '': {
            'level': 'WARNING',
            'handlers': ['stream', ],
        },
        'base': {
            'level': 'WARNING',
            'handlers': ['request_stream', ],
            'propagate': False,
        },
    },
}

# Caches
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
        'LOCATION': 'unix:/tmp/memcached.sock',
        'KEY_PREFIX': 'DEFAULT'
    },
    'sessions': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': 'unix:/tmp/memcached.sock',
        'KEY_PREFIX': 'SESSION'
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# EMAIL
EMAIL_HOST = 'smtp.qiye.aliyun.com'
EMAIL_USE_SSL = True
EMAIL_PORT = 465
EMAIL_TIMEOUT = 3
EMAIL_FAIL_RETRY = 3

EMAIL_COUNTER_KEY = 'email_counter'
EMAIL_COUNTER_DURATION = 7200

# Banner
BANNER_COUNT = 3


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')


# Upload location
# FIXME: this path shall be changed
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

UPLOAD_APPEARANCE_BANNER = 'upload/base/banner/%Y/%m/%d/'
UPLOAD_VALIDATE_PHOTO = 'upload/user/validate/%Y/%m/%d/'
UPLOAD_CATEGORY_ICON = 'upload/category/icon/'
QR_STORE_PATH = 'qr/'


# File Storage
DEFAULT_FILE_STORAGE = 'base.util.WLFileStorage.UUIDFileStorage'

# Phone Validator

PHONE_VALIDATOR = "base.util.sms.phone_validator.validator.DummyPhoneValidator"

SMS = "base.util.sms.sms.ConsolePrintSMS"

# String Validators

STRING_VALIDATORS = [
    {
        "NAME": "phone number",
        "CLASS": "base.util.misc_validators.PNValidator",
        "ARGS": {

        }
    },
    {
        "NAME": "user password",
        "CLASS": "base.util.misc_validators.DummyValidator",
    },
    {
        "NAME": "reason",
        "CLASS": "base.util.misc_validators.DummyValidator",
    }
]

# User_Sid duration
SID_DURATION = datetime.timedelta(days=10)

# Pusher
PUSHER = {
    "clz": "pushsys.funcs.pusher.jpusher.jpusher.JPusher",
    "kwargs": {}
}

# CORS Staffs

CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_ALLOW_ALL = True
CORS_ORIGIN_WHITELIST = (
    '*'
)

CORS_ALLOW_METHODS = (
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
    'VIEW',
)

CORS_ALLOW_HEADERS = (
    'XMLHttpRequest',
    'X_FILENAME',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
    'Pragma',
)

# history
SIMPLE_HISTORY_HISTORY_CHANGE_REASON_USE_TEXT_FIELD = True

# WCMiniProgram

MINIPROGRAM = {
    "AppID": 'wxfbbd60114365d79f',
    "AppSecret": '77dacbf01a0bedbf663a932a2e0de4a7',
}

TIME_FOR_SET_ORDER = 1800
TIME_FOR_DISPATCH = TIME_FOR_SET_ORDER / 2
COUNTDOWN_FOR_ORDER = 3600

NUM_OF_NEAR_BIN = 1000

BUDGET_MAX_CAN_CANCEL = decimal.Decimal('20.0')
COUNT_PER_PAGE = 10

# BB recycle settings
BBRECYCLE_CTX = {
    'bbtel': '0411-62623999',
    'exclude_sms': {'18888888888', }
}

ORDER_RESET_CREATE_TIME_DURATION = 600

# CELERY
CELERY_BROKER_URL = 'amqp://guest@localhost//'
# CELERY_RESULT_BACKEND = 'rpc://'
CELERY_IGNORE_RESULT = True
CELERY_ENABLE_UTC = False
CELERY_TIMEZONE = TIME_ZONE
CELERY_BEAT_SCHEDULER = 'django_celery_beat.schedulers:DatabaseScheduler'

# AntiDuplicatePostMiddleware
ANTI_DUP_POST_UUID_KEY = 'adp_uuid'
ANTI_DUP_POST_CACHE_USE = 'sessions'

# display order with referrer
DISPLAY_AMOUNT = 100