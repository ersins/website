"""
Django settings for app project.

Generated by 'django-admin startproject' using Django 3.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
from .keyconfig import SecretsEnv, DatabaseEnv, FolderRoots, DebugEnv, AllowedHostEnv, CeleryEnv, EpostaEnv
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

SECRET_KEY = SecretsEnv.SECRET_KEY

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True
DEBUG = DebugEnv.DEDUG

# ALLOWED_HOSTS = ['0.0.0.0', 'localhost', '127.0.0.1']
ALLOWED_HOSTS = AllowedHostEnv.ALLOWED_HOSTS

# Eposta Gönderim ayarları
EMAIL_HOST = EpostaEnv.EMAIL_HOST
EMAIL_HOST_USER = EpostaEnv.EMAIL_HOST_USER
EMAIL_HOST_PASSWORD = EpostaEnv.EMAIL_HOST_PASSWORD
EMAIL_PORT = EpostaEnv.EMAIL_PORT
EMAIL_USE_TLS = EpostaEnv.EMAIL_USE_TLS

DEFAULT_FROM_EMAIL = 'Klikya eCommerce <esenzek@gmail.com>'

BASE_URL = '127.0.0.1:8000'

MANAGERS = (
    ('Ersin Senzek', "ersinsenzek@gmail.com"),
)
ADMINS = MANAGERS

# User activation Süresi 7 olarak ayarlandı

DEFAULT_ACTIVATION_DAYS = 7

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'crispy_forms',

    'accounts.apps.AccountsConfig',
]

AUTH_USER_MODEL = 'accounts.User'  # changes the built-in user model to ours
LOGIN_URL = '/login/'
LOGIN_URL_REDIRECT = '/'
LOGOUT_URL = '/logout/'

FORCE_SESSION_TO_ONE = False
FORCE_INACTIVE_USER_END_SESSION = False

# Redis url
# CELERY_BROKER_URL = 'amqp://esmayan:1qazxsw234@localhost:5672/pydev-vhost'
CELERY_BROKER_URL = CeleryEnv.CELERY_BROKER
CELERY_RESULT_BACKEND = CeleryEnv.CELERY_BACKEND

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

LOGOUT_REDIRECT_URL = '/login/'
ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': FolderRoots.get_template_dirs(BASE_DIR),
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

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': BASE_DIR / 'db.sqlite3',
#    },
    'default': {
        'ENGINE': "django.db.backends.postgresql",
        'NAME': DatabaseEnv.NAME,
        'USER': DatabaseEnv.USER,
        'PASSWORD': DatabaseEnv.PASSWORD,
        'HOST': DatabaseEnv.HOST,
        'PORT': DatabaseEnv.PORT,
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'tr'

TIME_ZONE = 'Europe/Istanbul'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    FolderRoots.get_staticfiles_root(BASE_DIR),
]


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# IMPORT_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static_cdn", "import_root")

STATIC_ROOT = FolderRoots.get_static_root(BASE_DIR)

MEDIA_URL = '/media/'
MEDIA_ROOT = FolderRoots.get_media_root(BASE_DIR)

PROTECTED_ROOT = FolderRoots.get_protected_root(BASE_DIR)
