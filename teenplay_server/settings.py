"""
Django settings for teenplay_server project.

Generated by 'django-admin startproject' using Django 5.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""
import os
from pathlib import Path

import sys

# 요청의 데이터 크기 제한 설정
DATA_UPLOAD_MAX_MEMORY_SIZE = 1024 * 1024 * 10

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-ae#4x$6v8%w$ltg(5hdq43$*=+1_v@451gj$2j&t++x9#9o01h'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1', 'localhost','15.165.218.32', 'teenplay.shop']


# Application definition

INSTALLED_APPS = [
    'main',
    'oauth',
    'search',
    'friend',
    'letter',
    'alarm',
    'notice',
    'wishlist',
    'activity',
    'pay',
    'festival',
    'teenplay',
    'club',
    'member',
    'teenplay_server',
    'django_cron',
    'django_crontab',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.kakao',
    'allauth.socialaccount.providers.naver',
    'allauth.socialaccount.providers.google',
    'rest_framework'
]

CRONJOBS = [
    ('0 0 * * *', 'activity.tasks.DeleteOldImages')
]

SITE_ID = 3

SOCIALACCOUNT_AUTO_SIGNUP = True
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_LOGOUT_ON_GET = True

LOGIN_REDIRECT_URL = '/oauth/login/'

ACCOUNT_LOGOUT_REDIRECT_URL = '/'

AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',
    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
]

MIDDLEWARE = [
    'django_user_agents.middleware.UserAgentMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'allauth.account.middleware.AccountMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'teenplay_server.middleware.pre_handle_request'
]

ROOT_URLCONF = 'teenplay_server.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
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

WSGI_APPLICATION = 'teenplay_server.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        # DBMS 모듈 경로
        'ENGINE': 'django.db.backends.mysql',
        # DATABASE 이름
        'NAME': 'teenplay',
        # 계정 이름
        'USER': 'project',
        # 계정 비밀번호
        'PASSWORD': '1234',
        # DBMS가 설치된 서버 PC의 IP, (127.0.0.1 = 로컬)
        'HOST': '3.34.127.23',
        # DBMS의 포트번호
        'PORT': '3306'
    }
}



# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

LANGUAGES = (
    ("ko", "Korean"),
    ("en", "English"),
)

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# 파일 접근 시
MEDIA_URL = '/upload/'

# 파일 업로드 시
MEDIA_ROOT = os.path.join(BASE_DIR, 'upload')

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
