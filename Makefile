.DEFAULT_GOAL := help

base_python := python3
python := $(py) python
project_source_dir := src

reports_dir := reports


# =================================================================================================
# Environment
# =================================================================================================

.PHONY: install
install:
	$(base_python) -m pip install -r requirements.txt

.PHONY: clean
clean:
	rm -rf `find . -name __pycache__`
	rm -f `find . -type f -name '*.py[co]' `
	rm -f `find . -type f -name '*~' `
	rm -f `find . -type f -name '.*~' `
	rm -rf `find . -name .pytest_cache`
	rm -rf *.egg-info
	rm -f .coverage
	rm -f report.html
	rm -f .coverage.*
	rm -rf {build,dist,site,.cache,.mypy_cache,reports}


# =================================================================================================
# Code quality
# =================================================================================================

.PHONY: isort
isort:
	$(py) isort -rc $(project_source_dir)

.PHONY: black
black:
	$(py) black $(project_source_dir)

.PHONY: flake8
flake8:
	$(py) flake8 $(project_source_dir)

.PHONY: flake8-report
flake8-report:
	mkdir -p $(reports_dir)/flake8
	$(py) flake8 --format=html --htmldir=$(reports_dir)/flake8 $(project_source_dir)

.PHONY: lint
lint: isort black flake8 mypy
