import environ

from .base import *


env = environ.Env()
environ.Env.read_env(BASE_DIR / ".env")
SECRET_KEY = env("SECRET_KEY")
DEBUG = True
ALLOWED_HOSTS = [
    "localhost",
    "127.0.0.1",
]
DATABASES = {
    "default": {
        "ENGINE": "",
        "NAME": "",
        "USER": "",
        "PASSWORD": "",
        "HOST": "",
        "PORT": "",
    }
}
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://localhost:8000",
    "http://127.0.0.1:3000",
    "http://127.0.0.1:8000",
]
