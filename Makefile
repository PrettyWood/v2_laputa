test:
	PYTHONPATH=. pytest --cov-report term-missing --cov=api tests/ -v
