import os.path
import sys
import django

from django.conf import settings

settings.configure(
    DATABASES={
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(os.path.dirname(__file__), 'testdb.sqlite'),
        }
    },
    CACHES={
        'default': {
            'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        }
    },
    INSTALLED_APPS=('chunks',),
    TEMPLATES=[
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [],
            'APP_DIRS': True,
            'OPTIONS': {
                # ... some options here ...
            },
        },
    ]
)

django.setup()
from django.test.utils import get_runner

test_runner = get_runner(settings)()
failures = test_runner.run_tests(['chunks'])

sys.exit(failures)
