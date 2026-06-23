.PHONY: preview test

preview:
	python3 tools/preview_server.py

test:
	python3 -m unittest discover -s tests -q
