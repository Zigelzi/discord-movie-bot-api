from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('api.config.Config')

db = SQLAlchemy(app)

# Flask-Marshmallow is used for serializing the DB objects to JSON.
ma = Marshmallow(app)

CORS(app, resources={r'/*': {'origins': '*'}})

from api import routes, models