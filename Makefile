.PHONY: no_targets


no_targets:
	echo "command expected"

prod_up:
	LOCAL_USER_ID=$$(id -u) LOCAL_GROUP_ID=$$(id -g) docker-compose up --build

prod_down:
	LOCAL_USER_ID=$$(id -u) LOCAL_GROUP_ID=$$(id -g) docker-compose down -v

dev_up:
	LOCAL_USER_ID=$$(id -u) LOCAL_GROUP_ID=$$(id -g) docker-compose -f docker-compose-dev.yml up --build

dev_down:
	LOCAL_USER_ID=$$(id -u) LOCAL_GROUP_ID=$$(id -g) docker-compose -f docker-compose-dev.yml down -v

dev_run:
	python manage.py makemigrations --no-input
	python manage.py migrate --no-input
	python manage.py runserver 0.0.0.0:8000
	python manage.py runapscheduler