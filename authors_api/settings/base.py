from pathlib import Path
import environ

env=environ.Env()
# Build paths inside the project like this: BASE_DIR / 'subdir'.

ROOT_DIR= Path(__file__).resolve().parent.parent.parent

APPS_DIR=ROOT_DIR / "core_apps"


DEBUG = env.bool("DJANGO_DEBUG", False)

ALLOWED_HOSTS = []


# Application definition

DJANGO_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
]
THIRD_PARTY_APPS=[
    "rest_framework",
    "django_filters",
    "django_countries",
    "phonenumber_field",
    "drf_yasg",
    "corsheaders"
]

LOCAL_APPS=[
    "core_apps.common",
    "core_apps.profiles",
    "core_apps.users",
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'authors_api.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [str(APPS_DIR/"templates")],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.i18n',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'authors_api.wsgi.application'


DATABASES = {"default": env.db("DATABASE_URL")}
DATABASES["default"]["ATOMIC_REQUESTS"] = True

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators
PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.Argon2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
]
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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True#장고 번역 시스템 활성 여부 설정
USE_L10N=True#현지화 데이터 형식 사용 여부 설정
USE_TZ = True#시간대 인식 여부 설정

SITE_ID=1  
#원하는 URL을 1번으로 등록할 수 있음 
#비슷함 콘텐츠나 기능을 가진 웹사이트가 
# 여러개 필요할때는 장고 프로젝트 하나로 여러 사이트를 운영할 있고 
# 이때 'SITE_ID=번호'를 사용할 수 있어 
ADMIN_URL = "supersecret/"
ADMINS = [("""eungi""", "lovee2756@gmail.com")]
MANAGER = ADMINS

STATIC_URL = '/staticfiles/'
STATIC_ROOT= str(ROOT_DIR / 'staticfiles')
STATICFILES_DIRS=[]
STATFILES_FINDERS=[
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder"

]
MEDIA_URL = '/mediafiles/'
MEDIA_ROOT= str(ROOT_DIR / 'mediafiles')
# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CORS_URLS_REGEX=r"^/api/.*$"

