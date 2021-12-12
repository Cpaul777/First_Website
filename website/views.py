from flask import Blueprint, render_template

views = Blueprint('views', __name__)


@views.route('/')
def homepage():
    return "<h> big leap for the<br> MANKIND</h>"
