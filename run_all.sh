#!/bin/bash
#chmod +x run_all.sh
#./run_all.sh

python manage.py flush
python manage.py migrate
python manage.py fill_db_category
python manage.py fill_db_users
python manage.py fill_db_idea
python manage.py fill_db_comment
python manage.py fill_db_partnerships
python manage.py fill_db_notifications

python manage.py runserver