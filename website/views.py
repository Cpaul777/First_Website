from flask import Blueprint

views = Blueprint('views', __name__)


@views.route('/')
def homepage():
    return "<h> big leap for the<br> MANKIND</h>"
