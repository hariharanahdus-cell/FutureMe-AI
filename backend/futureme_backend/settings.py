import os
from pathlib import Path
import dj_database_url


BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = os.environ.get(
    "SECRET_KEY",
    "django-insecure-development-key"
)


DEBUG = False


ALLOWED_HOSTS = [
    "futureme-backend-a6ox.onrender.com",
    "localhost",
    "127.0.0.1"
]


# Applications

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    "rest_framework",
    "api",
]


MIDDLEWARE = [

    "corsheaders.middleware.CorsMiddleware",

    "django.middleware.security.SecurityMiddleware",

    "django.contrib.sessions.middleware.SessionMiddleware",

    "django.middleware.common.CommonMiddleware",

    "django.middleware.csrf.CsrfViewMiddleware",

    "django.contrib.auth.middleware.AuthenticationMiddleware",

    "django.contrib.messages.middleware.MessageMiddleware",

    "django.middleware.clickjacking.XFrameOptionsMiddleware",

]


ROOT_URLCONF = "futureme_backend.urls"



DATABASES = {

    "default": dj_database_url.config(

        default=os.environ.get("DATABASE_URL")

    )

}



# CORS

CORS_ALLOW_ALL_ORIGINS = True


# Later replace with your Vercel URL:

# CORS_ALLOWED_ORIGINS = [
#     "https://your-app.vercel.app"
# ]



# Static files

STATIC_URL = "static/"

STATIC_ROOT = BASE_DIR / "staticfiles"



DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]