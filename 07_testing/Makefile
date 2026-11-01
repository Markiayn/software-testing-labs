.PHONY: install test unit integration coverage html clean

install:
	poetry install

# Кожна частина запускається окремим процесом pytest: в обох частинах є модуль app.py,
# і в спільному процесі тести другої частини імпортували б Figure з першої.
test:
	poetry run pytest -v 01_general_and_unittest
	poetry run pytest -v 02_pytest

unit:
	poetry run pytest -m unit -v 02_pytest

integration:
	poetry run pytest -m integration -v

coverage:
	poetry run pytest --cov --cov-report=term-missing

html:
	poetry run pytest --cov --cov-report=html

clean:
	poetry run python -c "import shutil, pathlib; [shutil.rmtree(p, ignore_errors=True) for p in ('.pytest_cache', 'htmlcov')]; pathlib.Path('.coverage').unlink(missing_ok=True)"
