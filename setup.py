"""
Setup file for buckler
"""


import os
from setuptools import setup


def read(filename):
    """Read a filename as a string"""
    return open(os.path.join(os.path.dirname(__file__), filename)).read()


setup(
    name="buckler",
    version="0.1.0",
    author="Madelyn Eriksen",
    author_email="madelyn.eriksen@gmail.com",
    description="A simple command line password manager, "
                "using Scrypt and written in pure python",
    url="https://www.github.com/madelyneriksen/buckler",
    packages=[],
    long_description=read('README.md'),
)
