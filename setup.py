#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

setup(
    name='multidate',
    version='0.1.0',
    description="Process multiple timestamps, similar to the unix date tool.",
    author="Walter Menendez",
    author_email='menendezwalt@gmail.com',
    url='https://github.com/walterm/multidate',
    packages=find_packages(include=['multidate']),
    entry_points={
        'console_scripts': [
            'multidate=multidate.cli:main'
        ]
    },
)
