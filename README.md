# Devops

![master](https://github.com/birdi7/devops/actions/workflows/main.yml/badge.svg?branch=master)


This is my submission for the first lab of the DevOps course.

## Python app

Small flask web app, which shows current Moscow time on the webpage.
Uses [black](https://github.com/psf/black) and [isort](https://github.com/timothycrosley/isort) with [seed-isort-config](https://github.com/asottile/seed-isort-config) for code-formatting, and [flake8](http://flake8.pycqa.org/en/latest/) with [pylint](https://www.pylint.org) for linting. [Pre-commit](https://pre-commit.com) hooks are installed for every tool, except for the pylint.

### endpoint
— `localhost:5000/` - shows current time in moscow. writes visits into `/opt/data/visits.json`
— `localhost:5000/visits/` — shows content of `/opt/data/visits.json`


### Requirements

See [requirements.txt](requirements.txt).

### Quick start

1. Clone
  `git clone git@github.com:Birdi7/devops.git`
2. Create virtualenv.
    It's better if alias `python3` is set to `python3.7`,
    as I use it for the docker image
    `python3 -m virtualenv .venv`
3. Activate virtual env
    `. .venv/bin/activate`
4. Install packages
   `pip install -r requirements.txt`
5. Run app
    `cd app_python && flask run`

## Docker

1. Run with `docker run -it -p 5000:5000 birdi7/devops-1`
2. See `localhost:5000`

Build with `docker build -t=birdi7/devops-1 .`


## Unit Tests

1. Activate your virtual environment
2. Install development packages with
`pip install -r requirements-dev.txt`
3. Change current working directory with `cd app_python/`
4. Run `pytest`

## CI / CD

### Github Actions

The are a workflow file [main.yaml](.github/workflows/main.yml)

There are 2 jobs:
1. `lint_and_test`. It runs linters over the project, and executes unit-tests
2. `build` — builds docker image and push to the docker hub
with tag `birdi7/devops:latest`

There are 2 caches:
1. Docker layering cache. As specified [here](https://docs.docker.com/language/python/configure-ci-cd/)
2. Pip dependencies cache, as specified [here](https://docs.github.com/en/actions/guides/caching-dependencies-to-speed-up-workflows)
