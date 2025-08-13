install: 
	uv sync
build:
	uv build
.PHONY: gendiff
gendiff:
	uv run gendiff file1.json file2.json

lint:
	uv run ruff check gendiff --fix

install-tests:
	python -m pip install --upgrade pip
	python -m pip install pytest

check: 
	python -m pytest