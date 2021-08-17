# Best practices

1. Usage of linters on pre-commit hooks
    * black
    * isort 
    * flake8 
    * pylint (I prefer flake8, however)
2. Use `requirements.txt` and generate it with `pip freeze > requirements.txt`
3. Use pyproject.toml for plugin configuration purposes
4. Use Makefile for all repeated and complicated commands 
5. Use .gitignore 
6. Create local virtualenv for every project use have, or use manager of them (poetry, for instance)
