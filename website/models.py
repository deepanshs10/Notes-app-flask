from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
import sqlalchemy as sa

class Note(db.Model):
    id = sa.Column(sa.Integer, primary_key=True)
    data = sa.Column(sa.String(10000))
    date = sa.Column(sa.DateTime(timezone=True), default=func.now())
    user_id = sa.Column(sa.Integer, sa.ForeignKey('user.id'))

class User(db.Model, UserMixin):
    id = sa.Column(sa.Integer, primary_key=True)
    email = sa.Column(sa.String(150), unique=True)
    password = sa.Column(sa.String(150))
    first_name = sa.Column(sa.String(150))
    notes = db.relationship('Note')