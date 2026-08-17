# PythonAnywhere WSGI Configuration for foodiehub Django REST API
import os
import sys
from pathlib import Path

# Add project path to sys.path
path = '/home/yourusername/session-6'
if path not in sys.path:
    sys.path.insert(0, path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'foodiehub.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
