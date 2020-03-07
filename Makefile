define USAGE
Smart-Parking Setup

Commands:
	install   Install Python dependencies.
	init      Create migration repository
	migrate   Migrate flask model.
	start     Start flask app (development)
endef

export USAGE
help:
	@echo "$$USAGE"

python-packages:
	pip install -r requirements.txt

install:python-packages

init:
	export FLASK_ENV=development
	export FLASK_APP=run.py
	flask db init

migrate:
	flask db migrate
	flask db upgrade

start:
	flask run
