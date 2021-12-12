from flask import Blueprint

auth = Blueprint('auth', __name__)

@auth.route('sign-up')
def signing_up():
    return "<h1>hi</h1>"

@auth.route('login')
def login():
    return "<h1>NOT YET FINISHED</h1>"

@auth.route('chat')
def chat():
    return "<h1>GAGAWAN PALANG</h1>"
@auth.route('logout')
def logout():
    return "<h1>bye</h1>"
