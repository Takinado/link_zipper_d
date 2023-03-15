#! /bin/sh

if [ "$DATABASE" = "MYSQL" ]
then
    echo "Waiting for postgres..."
#    while ! nc -z $MYSQL_HOST $MYSQL_PORT; do
#      sleep .1
#    done
    echo "MySQL started"
fi
echo "$DATABASE"

sleep 15

python manage.py makemigrations --no-input
python manage.py migrate --no-input
python manage.py runserver 0.0.0.0:8000
python manage.py runapscheduler
