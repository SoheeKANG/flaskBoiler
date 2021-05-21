from flask import render_template, current_app
from .routes import homebp


@homebp.route('/')
def home():
    current_app.logger.info("home page loading")
    return render_template('home.html')
