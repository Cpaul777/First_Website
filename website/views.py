from flask import Blueprint

views = Blueprint('views', __name__)


@views.route('/')
def homepage():
    return "<h>  Did it work <br> If so NiceEee </h>"
