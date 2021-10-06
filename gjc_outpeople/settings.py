"""
Django settings for gjc_outpeople project.

Generated by 'django-admin startproject' using Django 3.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os
from pathlib import Path
from django.conf import settings

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-%in^qo&m)9v%&ritv0k985l_#-givpb07%*ubtu2j1_o^t_9#k'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
# DEBUG = False

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'simpleui',  # simpleui
    'import_export',  # 导入导出
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'outPeople.apps.OutpeopleConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'gjc_outpeople.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
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

WSGI_APPLICATION = 'gjc_outpeople.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'gjccgry',
        'HOST': '123.56.127.98',
        'PORT': '3306',
        'USER': 'gjccgry',
        'PASSWORD': 'gjccgry'
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]
STATIC_ROOT = os.path.join(BASE_DIR, "/static/")

# Simpleui 私有
SIMPLEUI_DEFAULT_ICON = False
SIMPLEUI_HOME_INFO = False
# SIMPLEUI_CONFIG = {
#     'system_keep': True,  # 关闭系统默认
#
#     # 菜单名
#     'menu_display': ['信息登记', '用户与权限'],
#     'dynamic': True,  # 设置是否开启动态菜单, 默认为False. 如果开启, 则会在每次用户登陆时动态展示菜单内容
#
#     'menus': [
#         {
#             'app': 'outPeople',
#             'name': '信息登记',
#             'icon': 'fas fa-code',
#             'models': [
#                 {
#                     'name': '教师信息登记',
#                     'icon': 'fa fa-user',
#                     # 渲染数据表菜单
#                     'url': '/admin/outPeople/t_info/'
#                 },
#                 {
#                     'name': '学生信息登记',
#                     'icon': 'fa fa-user',
#                     # 渲染数据表菜单
#                     'url': '/admin/outPeople/s_info/'
#                 },
#                 {
#                     'name': '出国信息登记',
#                     'icon': 'fa fa-user',
#                     # 渲染数据表菜单
#                     'url': '/admin/outPeople/outcheckin/'
#                 }
#             ]
#         },
#         {
#             'app': 'auth',
#             'name': '用户与权限',
#             'icon': 'fas fa-user-shield',
#             'models': [
#                 {
#                     'name': '用户',
#                     'icon': 'fa fa-user',
#                     'url': 'auth/user/'
#                 },
#                 {
#                     'name': '用户组',
#                     'icon': 'fa fa-user',
#                     'url': 'auth/group/'
#                 }
#             ]
#         },
#
#     ]
# }
