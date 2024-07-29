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

test:
	python manage.py test

check_ports:
	sudo lsof -i :5432

kill_process:
	sudo kill <PID>

stop_all_containers:
	docker stop $(docker ps -aq)

remove_all_containers:
	docker rm $(docker ps -aq)

remove_all_images:
	docker rmi $(docker images -q)

remove_all_volumes:
	docker volume rm $(docker volume ls -q)

remove_all_networks:
	docker network rm $(docker network ls -q)

remove_all_unused_data:
	docker system prune -a --volumes
