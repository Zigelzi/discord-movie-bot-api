from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    movie_suggestion = {
        'name': 'Test Movie',
        'service': 'Netflix',
        'suggested_by': 'Dvh'
    }
    return jsonify(movie_suggestion)