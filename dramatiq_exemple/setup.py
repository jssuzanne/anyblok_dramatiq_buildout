#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Setup script for dramatiq"""

from setuptools import setup, find_packages
version = '1.0.0'

requirements = [
    'anyblok_dramatiq',
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='dramatiq_exemple',
    version=version,
    description="test simple usecase between anyblok and dramatiq",
    long_description='\n\n',
    author="jssuzanne",
    author_email='jssuzanne@anybox.fr',
    url='https://github.com/jssuzanne/dramatiq',
    packages=find_packages(),
    entry_points={
        'bloks': [
            'dramatiq_exemple=dramatiq_exemple.dramatiq:DramatiqExemple'
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    zip_safe=False,
    keywords='dramatiq',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],
    test_suite='tests',
    tests_require=test_requirements,
)
