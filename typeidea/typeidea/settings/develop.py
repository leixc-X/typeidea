from .base import *     # NOQA
"""
# NOQA的目的是告诉规范检测工具，这个地方不需要检测 
"""

DEBUG = True

DATABASES = {
    'default':{
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}