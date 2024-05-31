from .base import *
from .base import env

SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    default="django-insecure-w(fbaj*e43q9@y&9d2nm21+8i-ld@d=aim0u@nkgpsjr7-h53^",
)

DEBUG = True

CSRF_TRUSTED_ORIGINS = ["http://localhost:8080", "http://0.0.0.0:8080"]

CORS_ALLOW_ALL_ORIGINS = True

ALLOWED_HOSTS = ["0.0.0.0", "localhost"]
