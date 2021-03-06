#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

echo "Creating and seeing database tables..."
python manage.py create_db
python manage.py seed_db
echo "Tables created and seeded"

exec "$@"
