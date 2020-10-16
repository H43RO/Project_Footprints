"""
Django settings for footprint project.
Generated by 'django-admin startproject' using Django 3.0.8.
For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""
import os
import json
import sys
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

ROOT_DIR = os.path.dirname(BASE_DIR)
SECRET_PATH = os.path.join(ROOT_DIR, '.footprint_secret')
SECRET_BASE_FILE = os.path.join(BASE_DIR, 'secrets.json')

secrets = json.loads(open(SECRET_BASE_FILE).read())
for key, value in secrets.items():
    setattr(sys.modules[__name__], key, value)


ALLOWED_HOSTS = ['*']
# Application definition
AUTH_USER_MODEL = 'accounts.User'
INSTALLED_APPS = [
    'grappelli',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'django_filters',
    'rangefilter',
    'rest_registration',
    'rest_framework.authtoken',
    'crispy_forms',
    'ckeditor_uploader',
    'ckeditor',
    # My app
    'accounts',
    'histories',
    'places',
    'posts',
    'django_cleanup',
]

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [

    ],
    'DEFAULT_FILTER_BACKENDS': ('django_filters.rest_framework.DjangoFilterBackend',),
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ]    
}

# 유저 Api 대응 시 사용(로그인, 회원가입 등)
# Docuemnt : https://django-rest-registration.readthedocs.io/en/latest/
# body, subject 내용 바꿀 시에, 새로 venv 다운받을 시 venv/Lib/site-packages/rest_registration/templates/rest_registration/register/ 수정
REST_REGISTRATION = {
    'REGISTER_VERIFICATION_ENABLED': True,
    'REGISTER_EMAIL_VERIFICATION_ENABLED': False,
    'RESET_PASSWORD_VERIFICATION_ENABLED': True,
    'REGISTER_VERIFICATION_EMAIL_TEMPLATES' : {'subject' : "rest_registration/register/subject.txt", 'html_body' : 'rest_registration/register/body.html'},  
    'REGISTER_VERIFICATION_URL': ('http://127.0.0.1:8000/api_activate/'),
    'VERIFICATION_FROM_EMAIL' : 'sch.iot.esc@gmail.com',
    'SEND_RESET_PASSWORD_LINK_SERIALIZER_USE_EMAIL' : True,
    'RESET_PASSWORD_VERIFICATION_URL' : ('http://127.0.0.1:8000/api_password/'),
    'RESET_PASSWORD_VERIFICATION_EMAIL_REMPLATES' : {'html_body': 'rest_registration/reset_password/body.html', 'subject': 'rest_registration/reset_password/subject.txt'}, 
    'USER_LOGIN_FIELDS' :  ['email'],
    'SUCCESS_RESPONSE_BUILDER' : ('accounts.serializers.build_default_success_response'),
    'LOGIN_SERIALIZER_CLASS' : ('accounts.serializers.UserLoginSerializer'),
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',

]



ROOT_URLCONF = 'footprint.urls'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
WSGI_APPLICATION = 'footprint.wsgi.application'

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators
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
# https://docs.djangoproject.com/en/3.0/topics/i18n/
LANGUAGE_CODE = 'en-us'


TIME_ZONE = 'Asia/Seoul'

# USE_I18N = True
#
# USE_L10N = True
#
# USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# 이메일 인증을 위한 smtp 설정
AUTHENTICATION_BACKENDS = ['accounts.backend.EmailAuthBackend']
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587

EMAIL_USE_TLS = True

#로그인 세션 유지
SESSION_COOKIE_AGE = 60 * 60
SESSION_SAVE_EVERY_REQUEST = True

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
CKEDITOR_UPLOAD_PATH = "uploads/"