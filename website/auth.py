from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)

@auth.route('sign-up')
def signing_up():
    return render_template("signUp.html", )

@auth.route('login')
def login():
    return render_template("login.html", )

@auth.route('chat')
def chat():
    return "<h1>GAGAWAN PALANG</h1>"
@auth.route('logout')
def logout():
    return "<h1>bye</h1>"
