# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name="XML2XLSX",
    version="0.1",
    description="XMLish API for OpenPyXL",
    url="http://github.com/sq6jnx/xml2xlsx",
    author="Michał Sadowski",
    license="MIT/Expat (like OpenPyXL)",
    packages=["xml2xlsx"],
    install_requires=[
        "lxml",
        "openpyxl",
    ],
    tests_requires=[
        "lxml",
        "pytest",
        "openpyxl",
    ],
    zip_safe=False,
)
