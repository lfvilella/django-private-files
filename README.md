# django-private-files
Simple Django project showing how to have private static/media files

## Running the project

Make sure you have [Docker](https://docs.docker.com/get-docker/) and [docker-compose](https://docs.docker.com/compose/install/) installed then [run the project](#starting-the-server).


## Starting the server

    $ docker-compose build && docker-compose up


## Creating a super user

After [start the server](#starting-the-server) then run the command:

    $ docker-compose exec backend python manage.py createsuperuser

## Private files

Files at `app > frontend > static > private` will be only available for logged user.

## Django collect statics

    $ docker-compose exec backend python manage.py collectstatic --no-input