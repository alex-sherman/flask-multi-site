from flask import Blueprint, render_template
mod = Blueprint('sample', __name__, url_prefix='/sample', template_folder="templates", static_folder="static")

@mod.route('/')
def index():
    return "This is a sample blueprint for a Flask application with multiple Blueprints."