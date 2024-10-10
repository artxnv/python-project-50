.PHONY: lint install test coverage

install:
	poetry install
	curl -sSL https://install.python-poetry.org | python3 -
	echo "$$HOME/.local/bin" >> $$GITHUB_PATH

lint:
	poetry run flake8 .
	poetry run isort --check .

test:
	pytest --cov=. --cov-report=lcov --cov-report=term

coverage:
	./cc-reporter before-build
	pytest --cov=. --cov-report=lcov --cov-report=term --cov-report=lcov:coverage/lcov.info
	./cc-reporter after-build --exit-code $$? --coverage-input-type lcov --debug -p .

