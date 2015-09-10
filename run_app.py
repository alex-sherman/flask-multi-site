#!/usr/bin/python
# Run a test server.
from web_apps.app import App
App.run(host='0.0.0.0', port=8080, debug=True)