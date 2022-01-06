from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


# Note the quoted comments below are not yet used, and the triple quoted comments are gonna be many to one


"""class Chat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(250))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
     """


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship("Note")


# below
"""class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(250))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    first_name = db.Column(db.String(100), unique=True)
    notes = db.relationship("Note")"""


"""chat_id = db.Column(db.Integer, ForeignKey('wChat.db'))
     chat = db.relationship('Chat.db')"""
