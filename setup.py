#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from __future__ import absolute_import, print_function

import glob
import io
import re
from os.path import basename
from os.path import dirname
from os.path import join
from os.path import splitext

from setuptools import setup, find_packages


def read(*names, **kwargs):
    return io.open(
        join(dirname(__file__), *names),
        encoding=kwargs.get("encoding", "utf8")
    ).read()


setup(
    name='trainqlearning',
    version='0.1.0',
    license='BSD',
    description='This is a toy reinforcement learning project',
    long_description=re.compile('^.. start-badges.*^.. end-badges', re.M | re.S).sub('', read('README.md')),
    author='Ionel Cristian Mărieș',
    author_email='contact@ionelmc.ro',
    url='https://github.com/ionelmc/python-nameless',
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    py_modules=[splitext(basename(i))[0] for i in glob.glob("src/*.py")],
    keywords=[
    ],
    install_requires=[
    ],
    extras_require={
    },
)
