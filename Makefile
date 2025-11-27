.PHONY: install test lint examples clean

install:
	pip install -r requirements.txt

test:
	python scripts/run_tests.py

lint:
	flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics

examples:
	python scripts/run_all_examples.py

clean:
	find . -type d -name __pycache__ -exec rm -r {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete

all: install test lint examples

