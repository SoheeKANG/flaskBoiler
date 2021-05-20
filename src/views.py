from .routes import homebp
from flask import render_template, request, redirect, url_for, current_app


@homebp.route('/')
def home():
    current_app.logger.info("home page loading")
    return render_template('home.html')
