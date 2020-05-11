#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Setup script for PyWeights

You can install PyWeights with

python setup.py install
"""
from setuptools import setup
from os import path

DIR = path.dirname(path.abspath(__file__))

DESCRIPTION = "PyWeights (wt) is a Python package for the weighting, scoring, and evaluating of comprehensive system."

AUTHORS = 'Xia Tian'

URL = 'https://github.com/xSumner/pyweights'

EMAIL = 'xsumner@hotmail.com'

with open(path.join(DIR, 'requirements.txt')) as f:
    INSTALL_PACKAGES = f.read().splitlines()

with open(path.join(DIR, 'README.md')) as f:
    README = f.read()

# get __version__ from _version.py
ver_file = path.join('pyweights', '_version.py')
with open(ver_file) as f:
    exec(f.read())

VERSION = __version__

packages=["pyweights",
          "pyweights.algorithms"]

# add the tests
package_data     = {
    'pyweights': ['tests/*.py'],
    'pyweights.algorithms': ['tests/*.py']
    }


setup(
    name='pyweights',
    packages=['pyweights'],
    description=DESCRIPTION,
    long_description=README,
    long_description_content_type='text/markdown',
    install_requires=INSTALL_PACKAGES,
    version=VERSION,
    url=URL,
    author=AUTHORS,
    author_email=EMAIL,
    keywords=['weighting', 'scoring', 'comprehensive system'],
    tests_require=['pytest',],
    packages=packages,
    package_data=package_data,
    include_package_data=True,
    python_requires='>=3'
)
