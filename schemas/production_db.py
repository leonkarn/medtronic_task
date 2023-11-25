from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@db:5432/production_db'
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    join_year = db.Column(db.Integer, nullable=False)
    hobbies = db.relationship('Hobby', secondary='user_hobbies', back_populates='users')


class Hobby(db.Model):
    __tablename__ = 'hobbies'
    hobby_id = db.Column(db.Integer, primary_key=True)
    hobby_name = db.Column(db.String, nullable=False)
    users = db.relationship('User', secondary='user_hobbies', back_populates='hobbies')


class UserHobbies(db.Model):
    __tablename__ = 'user_hobbies'
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), primary_key=True)
    hobby_id = db.Column(db.Integer, db.ForeignKey('hobbies.hobby_id'), primary_key=True)
