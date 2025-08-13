install: 
	uv sync
build:
	uv build
.PHONY: gendiff
gendiff:
	uv run gendiff file1.json file2.json

lint:
	uv run ruff check gendiff --fix

pytest:
	pip install pytest

check: 
	python -m pytest