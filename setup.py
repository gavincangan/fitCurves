#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

# Load version from __init__.py
__version__ = "Undefined"
for line in open('fitcurves/__init__.py'):
    if (line.startswith('__version__')):
        exec(line.strip())

config = {
    'name': 'fitcurves',
    'author': 'Volker Poplawski',
    'author_email': 'volker@poplawski.de',
    'url': 'https://github.com/volkerp/fitCurves',
    'description': '''Python implementation of Philip J. Schneider's '''
        '''"Algorithm for Automatically Fitting Digitized Curves" from the '''
        '''book "Graphics Gems"''',
    'long_description': open('README.md', 'r').read(),
    'license': 'MIT',
    'version': __version__,
    'install_requires': [
        "numpy",
    ],
    'classifiers': [
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Development Status :: 1 - Planning",
    ],
    'packages': find_packages(),
}

if __name__ == '__main__':
    setup(**config)
