.PHONY: install test unit integration coverage html clean

install:
	poetry install

test:
	poetry run pytest -v

unit:
	poetry run pytest -m unit -v

integration:
	poetry run pytest -m integration -v

coverage:
	poetry run pytest --cov --cov-report=term-missing

html:
	poetry run pytest --cov --cov-report=html

clean:
	poetry run python -c "import shutil, pathlib; [shutil.rmtree(p, ignore_errors=True) for p in ('.pytest_cache', 'htmlcov')]; pathlib.Path('.coverage').unlink(missing_ok=True)"
