from api import db

from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

class MovieSuggestion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    message_id = db.Column(db.String(255), unique=True, nullable=False)
    name = db.Column(db.String(128), nullable=False)
    service = db.Column(db.String(128), nullable=False)
    suggested_by = db.Column(db.String(128), nullable=False)
    url = db.Column(db.String(255), nullable=False)
    votes = db.Column(db.Integer, default=0, nullable=False)
    watched = db.Column(db.Boolean(), default=False, nullable=False)
    
    def save(self):
        db.session.add(self)
    
    def delete(self):
        db.session.delete(self)

    @staticmethod
    def get_all():
        return MovieSuggestion.query.all()

# ---------------------------------
# Marshmallow serialization schemas
# ---------------------------------
class MovieSuggestionSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = MovieSuggestion
        load_instance = True
        sqla_session = db.session