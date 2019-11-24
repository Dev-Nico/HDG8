#!/bin/bash
source ~/.bashrc
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic
service apache2 restart
gunicorn servicioplanificacion.wsgi
