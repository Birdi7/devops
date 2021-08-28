# Best practices

I've chosen the Flask web framework as it's the most known
microframework in the Pythonic world for small web applications.

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

# Unit testing best practices

1. If you have an intuitive logic, try to use TDD — firstly write your tests, and only then start to code your main functionality
2. Avoid to mess up unit tests and integrative tests. Unit tests are meant to check the result of only one particular part
of a program
3. If some module is depended on the result of other, use `unittest.mock` module
in order to mock the behaviour of that other one
4. Try to make unit tests as small as possible. Avoid checking
several different usecases in one unit test
5. Cover the edge cases when writing some unit test
6. Group tests which checks the same part of the program
in the similar location
