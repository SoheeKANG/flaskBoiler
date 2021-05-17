from flask import Flask


def init_app():
    """Create Flask application"""
    app = Flask(__name__)
    app.config.from_pyfile('config.py')

    