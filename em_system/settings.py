import os
from pathlib import Path

from configurations import Configuration
from configurations.values import BooleanValue
from configurations.values import SecretValue
from dotenv import load_dotenv

load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


class Base(Configuration):
    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY: str = SecretValue(environ_prefix="", environ_required=True)

    # SECURITY WARNING: don't run with debug turned on in production!
    DEBUG: bool = BooleanValue(environ_prefix="", default=False)

    ALLOWED_HOSTS: list[str] = []

    # Application definition

    INSTALLED_APPS: list[str] = [
        "django.contrib.admin",
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.sessions",
        "django.contrib.messages",
        "django.contrib.staticfiles",
    ]

    MIDDLEWARE: list[str] = [
        "django.middleware.security.SecurityMiddleware",
        "django.contrib.sessions.middleware.SessionMiddleware",
        "django.middleware.common.CommonMiddleware",
        "django.middleware.csrf.CsrfViewMiddleware",
        "django.contrib.auth.middleware.AuthenticationMiddleware",
        "django.contrib.messages.middleware.MessageMiddleware",
        "django.middleware.clickjacking.XFrameOptionsMiddleware",
    ]

    ROOT_URLCONF: str = "em_system.urls"

    TEMPLATES: list[dict] = [
        {
            "BACKEND": "django.template.backends.django.DjangoTemplates",
            "DIRS": [os.path.join(BASE_DIR, "templates")],
            "APP_DIRS": True,
            "OPTIONS": {
                "context_processors": [
                    "django.template.context_processors.debug",
                    "django.template.context_processors.request",
                    "django.template.context_processors.media",
                    "django.contrib.auth.context_processors.auth",
                    "django.contrib.messages.context_processors.messages",
                ],
            },
        },
    ]

    WSGI_APPLICATION: str = "em_system.wsgi.application"

    # Database
    # https://docs.djangoproject.com/en/5.2/ref/settings/#databases

    DATABASES: dict = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        },
    }

    # Password validation
    # https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

    AUTH_PASSWORD_VALIDATORS: list[dict] = [
        {
            "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",  # noqa: E501
        },
        {
            "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",  # noqa: E501
        },
        {
            "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",  # noqa: E501
        },
        {
            "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",  # noqa: E501
        },
    ]

    # Internationalization
    # https://docs.djangoproject.com/en/5.2/topics/i18n/

    LANGUAGE_CODE: str = "en-us"

    TIME_ZONE: str = "UTC"

    USE_I18N: bool = True

    USE_TZ: bool = True

    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/5.2/howto/static-files/

    STATIC_URL: str = "static/"
    STATIC_ROOT = os.path.join(BASE_DIR, "static")

    MEDIA_URL: str = "media/"
    MEDIA_ROOT: str = os.path.join(BASE_DIR, "media")

    # Default primary key field type
    # https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

    DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


class Development(Base):
    INSTALLED_APPS: list[str] = [
        *Base.INSTALLED_APPS,
        "debug_toolbar",
    ]

    MIDDLEWARE: list[str] = [
        *Base.MIDDLEWARE,
        "debug_toolbar.middleware.DebugToolbarMiddleware",
    ]
    INTERNAL_IPS: list[str] = ["127.0.0.1"]


class Test(Base):
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": ":memory:",
            "OPTIONS": {
                "timeout": 30,
            },
        },
    }

    TEST_RUNNER = "em_system.runner.PytestTestRunner"


class Production(Base):
    CSRF_COOKIE_SECURE: bool = True
    CSRF_COOKIE_HTTPONLY: bool = True
