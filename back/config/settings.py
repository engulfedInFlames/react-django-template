import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
ROOT_DIR = Path(__file__).resolve().parent.parent.parent


SECRET_KEY = str(os.environ.get("DJANGO_SECRET_KEY"))
DEBUG = str(os.environ.get("DEBUG")) == "1"

ALLOWED_HOSTS = str(os.environ.get("ALLOWED_HOSTS")).split(" ")

CORS_ORIGIN_WHITELIST = str(os.environ.get("CORS_ORIGIN_WHITELIST")).split(" ")

CSRF_TRUSTED_ORIGINS = str(os.environ.get("CSRF_TRUSTED_ORIGINS")).split(" ")

SYSTEM_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.sites",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

THIRD_PARTY_APPS = [
    "corsheaders",
    "rest_framework",
    "oauth2_provider",
    "social_django",
    "drf_social_oauth2",
]

CUSTOM_APPS = [
    "users.apps.UsersConfig",
    "timestamps.apps.TimestampsConfig",
]

INSTALLED_APPS = SYSTEM_APPS + THIRD_PARTY_APPS + CUSTOM_APPS

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "social_django.context_processors.backends",
                "social_django.context_processors.login_redirect",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"


DB_ENGINE = str(os.environ.get("POSTGRES_ENGINE"))
DB_NAME = str(os.environ.get("POSTGRES_NAME"))
DB_USER = str(os.environ.get("POSTGRES_USER"))
DB_PASSWORD = str(os.environ.get("POSTGRES_PASSWORD"))
DB_HOST = str(os.environ.get("POSTGRES_HOST"))
DB_PORT = str(os.environ.get("POSTGRES_PORT"))

IS_DB_AVAILABLE = all(
    [
        DB_ENGINE,
        DB_NAME,
        DB_USER,
        DB_PASSWORD,
        DB_HOST,
        DB_PORT,
    ]
)

IS_POSTGRES_READY = str(os.environ.get("POSTGRES_READY")) == "1"

if IS_DB_AVAILABLE and IS_POSTGRES_READY:
    DATABASES = {
        "default": {
            "ENGINE": DB_ENGINE,
            "NAME": DB_NAME,
            "USER": DB_USER,
            "PASSWORD": DB_PASSWORD,
            "HOST": DB_HOST,
            "PORT": DB_PORT,
        }
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }

# django-allauth & dj-rest-auth
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "oauth2_provider.contrib.rest_framework.OAuth2Authentication",
        "drf_social_oauth2.authentication.SocialAuthentication",
    ],
}

AUTHENTICATION_BACKENDS = (
    "drf_social_oauth2.backends.DjangoOAuth2",
    "django.contrib.auth.backends.ModelBackend",
)

DRFSO2_PROPRIETARY_BACKEND_NAME = (
    "My App"  # Name of the OAuth2 social backend. Default is "Django"
)
ACTIVATE_JWT = True  # Defaults is False

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


STATIC_URL = "static/"


DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


AUTH_USER_MODEL = "users.CustomUser"
