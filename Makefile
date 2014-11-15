.PHONY: prepare_env run test

prepare_env:
	python bootstrap.py
	bin/buildout
	mkdir var || touch var/db
	bin/django syncdb --noinput
	bin/django migrate manozodynas

run:
	bin/django migrate manozodynas
	bin/django runserver

test:
	bin/django test
