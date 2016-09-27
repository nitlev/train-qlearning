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
    url="https://github.com/nitlev/pyzmq-helloworld",
    author='Veltin DUPONT',
    author_email='veltind@gmail.com',
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: CI Tools',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3.5',
    ],
    keywords='deep-learning reinforcement-learning train',
    version='0.1.0',
    license='BSD',
    description='This is a toy reinforcement learning project',
    long_description=re.compile('^.. start-badges.*^.. end-badges', re.M | re.S).sub('', read('README.md')),
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    py_modules=[splitext(basename(i))[0] for i in glob.glob("src/*.py")],
    install_requires=[
    ],
    extras_require={
    },
)
