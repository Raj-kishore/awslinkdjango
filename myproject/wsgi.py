"""
WSGI config for myproject project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
#
# application = get_wsgi_application()

'''
https://stackoverflow.com/questions/5836674/why-does-debug-false-setting-make-my-django-static-files-access-fail

I have used pip install dj-static=0.0.6 for production  
'''

from django.core.wsgi import get_wsgi_application
from dj_static import Cling

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
application = Cling(get_wsgi_application())