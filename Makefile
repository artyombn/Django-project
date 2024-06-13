startproject:
	python -m django startproject <proj name> .

runserver:
	python manage.py runserver

startapp:
	python manage.py startapp <model name>

makemigrations:
	python manage.py makemigrations

apply migrate:
	python manage.py migrate

createsuperuser:
	python manage.py createsuperuser

runworker of the Celery:
	celery -A proj worker -l INFO
