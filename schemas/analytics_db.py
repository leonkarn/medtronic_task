from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@analytics_db:5432/analytics_db'
db = SQLAlchemy(app)

class UserHobby(db.Model):
    __tablename__ = 'hobbies_analysis'
    id = db.Column(db.Integer, primary_key=True)
    hobby_name = db.Column(db.String, nullable=False)
    join_year = db.Column(db.Integer, nullable=False)
