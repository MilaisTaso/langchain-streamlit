lint:
	poetry run flake8 src
format:
	poetry run black src
sort:
	poetry run isort src
