from flask import Blueprint, render_template

views = Blueprint("views", __name__)


<<<<<<< HEAD
@views.route('/home')
def homepage():
    return render_template("home.html")

@views.route('/about-us')
=======
@views.route("/")
def home():
    return render_template("home.html")


@views.route("about-us")
>>>>>>> a2ceb9ea8b3cc6001f4c675aeb42a6752ea9a19b
def aboutUs():
    return render_template(
        "aboutUs.html",
    )
