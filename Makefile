install: 
	uv sync
build:
	uv build
.PHONY: gendiff
gendiff:
	uv run gendiff file1.json file2.json

lint:
	uv run ruff check gendiff --fix

check:
	python -m pytest