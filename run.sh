#!/bin/bash

if [[ $1 = 'prod' ]]
then
    /deploy/app/manage.py collectstatic --no-input
    /deploy/app/manage.py migrate
    cd /deploy/app
    uwsgi --http :8000 --module app.wsgi --processes=5
else
    /deploy/app/manage.py migrate
    /deploy/app/manage.py runserver 0.0.0.0:8000
fi