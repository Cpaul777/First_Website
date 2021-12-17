from flask import Flask

# from flask_sqlalchemy import SQLAlchemy


def first_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "Ten Fold of Pillars"

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    return app
