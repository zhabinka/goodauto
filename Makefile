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

# TODO: https://github.com/django-extensions/django-extensions/blob/main/docs/shell_plus.rst#additional-imports
# https://stackoverflow.com/questions/3772260/how-to-reload-modules-in-django-shell
shell:
	poetry run python manage.py shell_plus --ipython

dbshell:
	poetry run python manage.py dbshell

load:
	poetry run python manage.py load_brands
