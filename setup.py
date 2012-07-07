#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name="event_handler",
    version="0.1.0",
    description="A simple event handler and dispatcher",
    author="David Litvak",
    author_email = "david.litvakb@gmail.com",
    license = "GPL v3",
    keywords = "Events Thrower Listener",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
    ],
    url='http://github.com/dlitvakb',
)
