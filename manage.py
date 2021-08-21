from flask.app import Flask
from flask.cli import FlaskGroup

from api import app, db
from api.models import SuggestedMovie

cli = FlaskGroup(app)

@cli.command('create_db')
def create_db():
    db.drop_all()
    db.create_all()
    db.session.commit()

@cli.command('seed_db')
def seed_db():
    suggested_movie = SuggestedMovie(
        message_id='123abc',
        name='Seeded Moovie',
        service='Netflix',
        suggested_by='Dvh',
        url='www.google.com',
        votes=0
    )
    db.session.add(suggested_movie)
    db.session.commit()

if __name__ == '__main__':
    cli()