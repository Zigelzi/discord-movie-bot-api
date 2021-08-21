from enum import unique
from api import db

class SuggestedMovie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    message_id = db.Column(db.String(255), unique=True, nullable=False)
    name = db.Column(db.String(128), nullable=False)
    service = db.Column(db.String(128), nullable=False)
    suggested_by = db.Column(db.String(128), nullable=False)
    url = db.Column(db.String(255), nullable=False)
    votes = db.Column(db.Integer, default=0, nullable=False)
    watched = db.Column(db.Boolean(), default=False, nullable=False)
    