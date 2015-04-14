#!/usr/bin/python
# Run a test server.
from web_apps import wsgi
wsgi.WebApp("app").run(host='0.0.0.0', port=8080, debug=True)