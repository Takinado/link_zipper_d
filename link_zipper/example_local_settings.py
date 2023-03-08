# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-***"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "link_zipper_dj_db",
        "USER": "root",
        "PASSWORD": "mysql_root_password",
        "HOST": "127.0.0.1",
        "PORT": "3306",
    }
}

SITE = "http://127.0.0.1:8000/s"
