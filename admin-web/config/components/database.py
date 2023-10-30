import os

from dotenv import load_dotenv


load_dotenv()
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('POSTGRES__DATABASE'),
        'USER': os.environ.get('POSTGRES__USER'),
        'PASSWORD': os.environ.get('POSTGRES__PASSWORD'),
        'HOST': os.environ.get('POSTGRES__HOST'),
        'PORT': os.environ.get('POSTGRES__PORT'),
        'OPTIONS': {
           'options': '-c search_path=public,content'
        }
    },
    'admin_template': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('POSTGRES__DATABASE'),
        'USER': os.environ.get('POSTGRES__USER'),
        'PASSWORD': os.environ.get('POSTGRES__PASSWORD'),
        'HOST': os.environ.get('POSTGRES__HOST', '127.0.0.1'),
        'PORT': os.environ.get('POSTGRES__PORT', 5432),
        'OPTIONS': {
           'options': '-c search_path=public,content'
        }
    }
}
