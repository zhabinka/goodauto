install:
	poetry install

run:
	poetry run python manage.py runserver

req:
	poetry export -f requirements.txt --output requirements.txt --without-hashes

deps:
	poetry update

deploy:
	git push heroku main

logs:
	heroku logs --tail

locale:
	poetry run django-admin makemessages -l ru

localecompile:
	poetry run django-admin compilemessages

migrations:
	poetry run python manage.py makemigrations

migrate:
	poetry run python manage.py migrate

shell:
	poetry run python manage.py shell

dbshell:
	poetry run python manage.py dbshell

load:
	poetry run python manage.py load_brands
	poetry run python manage.py load_url_types
	poetry run python manage.py load_providers
