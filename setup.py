#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages


def get_version(filename):
    """Extract the package version"""
    with open(filename) as in_fh:
        for line in in_fh:
            if line.startswith('__version__'):
                return line.split('=')[1].strip()[1:-1]
    raise ValueError("Cannot extract version from %s" % filename)


with open('README.rst') as readme_file:
    readme = readme_file.read()

requirements = []

dev_requirements = [
    'coverage', 'pytest', 'pytest-cov==2.5.0', 'pytest-xdist', 'twine', 'pep8',
    'flake8', 'wheel', 'sphinx', 'sphinx-autobuild', 'sphinx_rtd_theme']

version = get_version('./src/doi/__init__.py')

setup(
    author="Alejandro Gallo",
    author_email='aamsgallo@gmail.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    description="Python package to work with Document Object Identifier (doi)",
    install_requires=requirements,
    extras_require={
        'dev': dev_requirements,
    },
    license="GNU General Public License v3",
    long_description=readme,
    include_package_data=True,
    keywords='doi',
    name='python-doi',
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    url='https://github.com/alejandrogallo/doi',
    version=version,
    zip_safe=False,
)
