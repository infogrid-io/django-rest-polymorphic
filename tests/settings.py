DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

INSTALLED_APPS = [
    'django.contrib.contenttypes',
    'tests',
]

# TODO: [Django 3.2+] We don't need to define this anymore.
SECRET_KEY = '[insecure]'
