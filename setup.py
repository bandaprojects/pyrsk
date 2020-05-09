#!/usr/bin/env python3

import os
from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="rsk",
    version="0.0.1",
    author="The BandaProject Team",
    author_email="nantas.nardelli@gmail.com",
    description=(
        "A (probably crappy) multiplayer Risk clone "
        "written as a mean to teach Python"
    ),
    license="MIT",
    keywords="bantz experiment italian risk teaching",
    url="https://github.com/edran/pyrsk",
    packages=find_packages(),
    long_description=read("README.md"),
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Games/Entertainment :: Board Games",
    ],
)
