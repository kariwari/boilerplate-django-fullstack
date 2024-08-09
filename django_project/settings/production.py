from decouple import config

from django_project.settings.base import *  # noqa: F403


# https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-SECRET_KEY
SECRET_KEY = config("SECRET_KEY")

# https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = config("DEBUG", cast=bool)

# https://docs.djangoproject.com/en/dev/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ["example.com"]

CSRF_TRUSTED_ORIGINS = ["https://example.com"]

# For Docker/PostgreSQL usage uncomment this and comment the DATABASES config above
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": config("DB_NAME"),
        "USER": config("DB_USER"),
        "PASSWORD": config("DB_PASSWORD"),
        "HOST": config("DB_HOST"),
        "PORT": config("DB_PORT"),
    }
}

# https://github.com/rq/django-rq?tab=readme-ov-file#django-rq
RQ_QUEUES = {
    "default": {
        "HOST": config("REDIS_HOST"),
        "PORT": config("REDIS_PORT"),
        "DB": config("REDIS_DB"),
        "DEFAULT_TIMEOUT": 360,
    },
}
RQ_SHOW_ADMIN_LINK = True

STORAGES = {
    "default": {
        "BACKEND": "storages.backends.gcloud.GoogleCloudStorage",
        "OPTIONS": {"location": "media"},
    },
    "staticfiles": {
        "BACKEND": "storages.backends.gcloud.GoogleCloudStorage",
        "OPTIONS": {"location": "static"},
    },
}

# https://docs.djangoproject.com/en/dev/ref/settings/#media-url
MEDIA_URL = "/media/"

# https://docs.djangoproject.com/en/dev/ref/settings/#media-root
MEDIA_ROOT = BASE_DIR / "mediafiles"  # noqa: F405

# https://docs.djangoproject.com/en/dev/ref/settings/#static-root
STATIC_ROOT = BASE_DIR / "staticfiles"  # noqa: F405

# https://docs.djangoproject.com/en/dev/ref/settings/#static-url
STATIC_URL = "/static/"

# https://docs.djangoproject.com/en/dev/ref/contrib/sites/#enabling-the-sites-framework
SITE_ID = 1
