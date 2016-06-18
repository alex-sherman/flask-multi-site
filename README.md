flask-multi-site
================

This repository serves as the skeleton for a Flask application using multiple Blueprints to compartmentalize portions of a Flask app. 

All Blueprints stored in the web_apps/ directory will be imported if they are stored in a package named "mod_*" with a main module named controller.py. controller.py should have an attribute called mod which should be the instantiated Blueprint.

In this example, a Blueprint called "app" is also exmplicity used, by instantiating WebApp with implementation="app".