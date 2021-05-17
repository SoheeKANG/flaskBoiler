from flask import Blueprint
from flask import render_template, url_for
import os


home_bp = Blueprint(
    "home_bp", __name__, static_folder=os.path.abspath('../static'), template_folder=os.path.abspath('../templates')
)


@home_bp.route('/', methods=["GET"])
def home():
    return render_template(
        'index.html'
    )
