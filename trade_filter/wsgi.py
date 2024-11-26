import os
import sys

path = '/home/Kadam36/https://github.com/Kadam36/trading.git'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'trade_filter.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

