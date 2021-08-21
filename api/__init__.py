from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from api.models import SuggestedMovie

app = Flask(__name__)
app.config.from_object('api.config.Config')

db = SQLAlchemy(app)

@app.route('/')
def index():
    movie_suggestion = {
        'name': 'Test Movie',
        'service': 'Netflix',
        'suggested_by': 'Dvh'
    }
    return jsonify(movie_suggestion)