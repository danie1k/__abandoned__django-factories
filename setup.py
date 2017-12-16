from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='django-factories',
    version='0.1',
    description='Simple classes factories for Django Framework',
    long_description=long_description,
    url='https://github.com/danie1k/django-factories',
    author='Daniel Kuruc <dnk@dnk.net.pl>',
    author_email='dnk@dnk.net.pl',
    classifiers=[
        'Development Status :: 3 - Alpha',
    ],
    packages=find_packages(),
    install_requires=[
        'django>=1.10,<2.0',
    ],
    extras_require={
        'development': [
            'pep8==1.7.0',
            'pylint==1.7.2',
        ],
    },
)

