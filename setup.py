#!/usr/bin/env python
from setuptools import setup, find_packages

install_requires = [
    "bleach",
    "jinja2",
    "Django>=1.4",
    "django-jsonfield",
    "django-model-utils",
    "django-tastypie",
    "docutils",
    "isoweek",
    "lxml",
]

setup(
    name="crate.web",
    version="0.1",
    author="Donald Stufft",
    author_email="donald@crate.io",
    url="https://github.com/crateio/crate.web",
    description="crate.web is a Django app that provides the building blocks to build a Package Index Server.",
    license=open("LICENSE").read(),
    packages=find_packages(exclude=("tests",)),
    package_data={'': ['LICENSE', 'NOTICE']},
    include_package_data=True,
    install_requires=install_requires,
    zip_safe=False,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 2.7",
        "Operating System :: OS Independent",
    ],
)
