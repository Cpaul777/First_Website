from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db


auth = Blueprint("auth", __name__)


@auth.route("sign-up", methods=["GET", "POST"])
def signing_up():
    if request.method == "POST":
        email = request.form.get("email")
        first_name = request.form.get("username")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")

        if len(email) < 4:
            flash("Email must have atleast 4 or more characters.", category="error")
        elif len(first_name) < 4:
            flash("Username must have atleast 4 or more characters.", category="error")
        elif len(password1) < 6:
            flash("Password must have atleast 6 or more characters.", category="error")
        elif password1 != password2:
            flash("Password is not the same", category="error")
        else:
            new_user = User(
                email=email,
                first_name=first_name,
                password=generate_password_hash(password1, method="sha256"),
            )
            db.session.add(new_user)
            db.session.commit()

            flash("Account created!", category="success")
            return redirect(url_for("views.home"))

    return render_template(
        "signUp.html",
    )


@auth.route("login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
    return render_template(
        "login.html",
    )


@auth.route("chat")
def chat():
    return "<h1>GAGAWAN PALANG</h1>"


@auth.route("logout")
def logout():
    return render_template(
        "home.html",
    )
