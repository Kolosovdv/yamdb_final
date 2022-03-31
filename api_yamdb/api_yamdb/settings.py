import os 

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'p&l%385148kslhtyn^##a1)ilz@4zqj=rq&agdol^##zgl9(vs'

DEBUG = False

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions', 

    'django.contrib.messages', 

    'django.contrib.staticfiles', 

    'rest_framework', 

    'django_filters', 

    'rest_framework_simplejwt', 

    'api', 

    'reviews', 

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

ROOT_URLCONF = 'api_yamdb.urls' 

TEMPLATES_DIR = os.path.join(BASE_DIR, "templates") 

TEMPLATES = [ 

    { 

        'BACKEND': 'django.template.backends.django.DjangoTemplates', 

        'DIRS': [TEMPLATES_DIR], 

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

 

WSGI_APPLICATION = 'api_yamdb.wsgi.application' 


DATABASES = { 

    'default': { 

        'ENGINE': os.getenv('DB_ENGINE', default='django.db.backends.postgresql'), 

        'NAME': os.getenv('DB_NAME', default='postgres'), 

        'USER': os.getenv('POSTGRES_USER', default='yatube_user1'), 

        'PASSWORD': os.getenv('POSTGRES_PASSWORD', default='xxxyyyzzz'), 

        'HOST': os.getenv('DB_HOST', default='db'), 

        'PORT': os.getenv('DB_PORT', default='5432') 

    } 

} 

 

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

 

 

LANGUAGE_CODE = 'en-us' 

 

TIME_ZONE = 'UTC' 

 

USE_I18N = True 

 

USE_L10N = True 

 

USE_TZ = True 

 

STATIC_URL = '/static/' 

 

# STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static/'),) 

STATIC_ROOT = os.path.join(BASE_DIR, 'static') 

 

MEDIA_URL = '/media/' 

MEDIA_ROOT = os.path.join(BASE_DIR, 'media') 

 

REST_FRAMEWORK = { 

    'DEFAULT_AUTHENTICATION_CLASSES': ( 

        'rest_framework_simplejwt.authentication.JWTAuthentication', 

    ), 

    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination', 

    'PAGE_SIZE': 10, 

} 


AUTH_USER_MODEL = 'reviews.User' 

 

EMAIL_HOST = 'smtp.gmail.com' 

 

EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER') 

 

EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD') 

 

EMAIL_PORT = 587 

 

EMAIL_USE_TLS = True 

 

ROLES = { 

    'ADMIN_ROLE': 'admin', 

    'USER_ROLE': 'user', 

    'MODERATOR_ROLE': 'moderator', 

} 
