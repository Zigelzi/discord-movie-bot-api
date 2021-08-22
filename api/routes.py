from flask import make_response, jsonify, request
from traceback import print_exc

from api import app, db
from api.models import (MovieSuggestion, MovieSuggestionSchema)

# ---------------------------------
# Marshmallow serialization schemas
# ---------------------------------
movie_suggestion_schema = MovieSuggestionSchema()
many_movie_suggestion_schema = MovieSuggestionSchema(many=True)

# Status message descriptions
status_msg_fail = "fail"
status_msg_success = "success"

@app.route("/")
def index():
    movie_suggestion = {
        "name": "Test Movie",
        "service": "Netflix",
        "suggested_by": "Dvh"
    }
    return jsonify(movie_suggestion)

@app.route("/movie_suggestions/<string:message_id>", methods=["GET"])
def get_movie_suggestion(message_id):
    response_object = {"status": status_msg_success}
    
    print(message_id)
    movie_suggestion = MovieSuggestion.query.filter_by(message_id=message_id).first()
    print(movie_suggestion)
    try:
        if movie_suggestion:
            movie_suggestion_json = movie_suggestion_schema.dump(movie_suggestion)
            response_object["data"] = movie_suggestion_json
            response_object["message"] = "Movie suggestion queried successfully!"
            json_response = jsonify(response_object)
            return make_response(json_response, 200)
        elif movie_suggestion == None:
            response_object["status"] = status_msg_fail
            response_object["message"] = f"Movie suggestion wasn't found with this message id: {message_id}"
            json_response = jsonify(response_object)
            return make_response(json_response, 404)
    except Exception as e:
        print_exc()
        response_object['status'] = status_msg_fail
        response_object['message'] = 'Something went wrong when trying to update task'
        json_response = jsonify(response_object)
        return make_response(json_response, 400)

@app.route("/movie_suggestions", methods=["POST"])
def add_movie_suggestion():
    response_object = {"status": status_msg_success}
    
    try:
        request_data = request.get_json()
        movie_suggestion = movie_suggestion_schema.load(request_data)
        movie_suggestion.save()
        db.session.commit()
        response_object["data"] = movie_suggestion_schema.dump(movie_suggestion)
        response_object["message"] = "Movie suggestion added successfully!"
        json_response = jsonify(response_object)
        return make_response(json_response, 200)
    except Exception as e:
        print_exc()
        response_object["status"] = status_msg_fail
        response_object["message"] = "Something went wrong when trying to add movie suggestion"
        db.session.rollback()
        json_response = jsonify(response_object)
        return make_response(json_response, 400)