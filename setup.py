from hoiio import __version__, __author__, __author_email__

import os
from setuptools import setup, find_packages


setup(
    name = "hoiio",
    version = __version__,
    author = __author__,
    author_email = __author_email__,
    description = "Python SDK for Hoiio API",
    license = "MIT",
    keywords = "hoiio voice sms conference fax ivr",
    url = "http://developer.hoiio.com",
    install_requires = ["requests"],
    packages = find_packages(),
    classifiers = [
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.5",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Communications :: Telephony",
    ],
)
