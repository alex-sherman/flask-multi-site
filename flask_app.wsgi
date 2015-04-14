import sys
sys.path.insert(0, '/var/www/ibeacons')
from web_apps import wsgi
application = wsgi.WebApp("app")