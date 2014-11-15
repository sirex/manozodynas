# coding: utf-8

from __future__ import unicode_literals

try:
    import ConfigParser as configparser
except ImportError:
    import configparser

from os import path

from setuptools import find_packages
from setuptools import setup


here = path.abspath(path.dirname(__file__))


def get_requirements(versions_file, requirements):
    install_requires = []
    versions = configparser.ConfigParser()
    versions.read(path.join(here, versions_file))
    versions = dict({
        key.lower(): val
        for key, val in versions.items('versions')
    })
    for req in requirements:
        if req in versions:
            install_requires.append('%s==%s' % (req, versions[req]))
        else:
            install_requires.append(req)
    return install_requires


setup(
    name='manozodynas',
    version='0.1',
    url='http://manožodynas.lt',
    license='MIT',
    description=(
        'Evolving Lithuanian language dictionary used to create and '
        'verify Lithuanian language terms.'
    ),
    maintainer='Hack4LT',
    maintainer_email='info@hack4.lt',
    packages=find_packages(),
    install_requires=get_requirements('config/versions.cfg', [
        'factory_boy',
        'south',
        'webtest',
        'django',
        'django-nose',
        'django-debug-toolbar',
        'django-webtest',
    ]),
    classifiers=[
        # https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License'
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Natural Language :: Lithuanian',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: End Users/Desktop',
    ],
)
