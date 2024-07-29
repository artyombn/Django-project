#!/bin/bash
#chmod +x run_all.sh
#./run_all.sh

echo "Starting run_all.sh"

echo "Checking installed packages"
pip list

echo "Using migrations"
python manage.py flush --no-input
python manage.py migrate
echo "Migration done"

#echo "Filling DB"
#python manage.py fill_db_category
#python manage.py fill_db_users
#python manage.py fill_db_idea
#python manage.py fill_db_comment
#python manage.py fill_db_partnerships
#python manage.py fill_db_notifications
#echo "Filling DB done"

echo "Starting DJANGO"
exec gunicorn -b 0.0.0.0:8000 Brainwave.wsgi:application