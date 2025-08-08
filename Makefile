install: 
	uv sync
build:
	uv build
.PHONY: gendiff
gendiff:
	uv run gendiff /home/pacifisting/python-project-50/gendiff/scripts/file1.json /home/pacifisting/python-project-50/gendiff/scripts/file2.json