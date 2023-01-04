bot:
	poetry run bot
install:
	poetry install
lint:
	poetry run flake8 tbot_random_book
test:
	poetry run pytest
test-cov:
	poetry run pytest --cov=tbot_random_book --cov-report xml
