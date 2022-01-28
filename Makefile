BASE_DIR := src
RUN := poetry run
MANAGE_PY := $(RUN) $(BASE_DIR)/manage.py

run: superuser
	$(MANAGE_PY) runserver

migrations: config.yml
	$(MANAGE_PY) makemigrations

migrate: config.yml
	$(MANAGE_PY) migrate

lint:
	$(RUN) black $(BASE_DIR)
	$(RUN) pylint $(BASE_DIR)
	$(RUN) mypy $(BASE_DIR)

superuser: config.yml
	$(MANAGE_PY) shell -c "import createsuperuser"

test: config.yml
	poetry run coverage run $(BASE_DIR)/manage.py test tests --noinput --timing

build:
	docker-compose up --build
