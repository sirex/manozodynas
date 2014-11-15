.PHONY: run test

all: bin/django var/db

run: bin/django var/db
	bin/django runserver

test: bin/django
	bin/django test

bin/buildout:
	python bootstrap.py --version 2.2.5

bin/django: bin/buildout buildout.cfg setup.py
	bin/buildout

buildout.cfg:
	printf '[buildout]\nextends = config/env/development.cfg\n' > buildout.cfg

var:
	mkdir var

var/db: var
	bin/django syncdb --noinput --all
	bin/django migrate --fake
