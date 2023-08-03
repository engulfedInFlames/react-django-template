#!/bin/bash
SUPERUSER_EMAIL=${DJANGO_SUPERUSER_EMAIL}
SUPERUSER_PASSWORD=${DJANGO_SUPERUSER_PASSWORD}
SUPERUSER_USERNAME=${DJANGO_SUPERUSER_USERNAME}

cd /app/

export DJANGO_SUPERUSER_EMAIL=$SUPERUSER_EMAIL
export DJANGO_SUPERUSER_PASSWORD=$SUPERUSER_PASSWORD
export DJANGO_SUPERUSER_USERNAME=$SUPERUSER_USERNAME

/opt/venv/bin/python manage.py makemigrations --noinput
/opt/venv/bin/python manage.py migrate --noinput 
/opt/venv/bin/python manage.py createsuperuser --noinput || true