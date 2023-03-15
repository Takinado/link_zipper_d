.PHONY: no_targets


no_targets:
	echo "command expected"

produp:
	docker-compose -f docker-compose.yml up --build

proddown:
	docker-compose -f docker-compose.yml down -v

up:
	docker-compose -f docker-compose-dev.yml up --build

down:
	docker-compose -f docker-compose-dev.yml down -v

run:
	python manage.py makemigrations --no-input
	python manage.py migrate --no-input
	python manage.py runserver 0.0.0.0:8000
	python manage.py runapscheduler