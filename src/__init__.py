import os
from flask import Flask
from .routes import homebp


def init_app():
    """Create Flask application"""
    app = Flask(__name__)
    app.register_blueprint(homebp)
    app.config.from_pyfile('config.py')

    return app
