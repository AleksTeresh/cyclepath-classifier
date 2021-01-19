#!/usr/bin/env python
import os
from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='cyclepath-classifier',
    version='0.1.0',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/AleksTeresh/cyclepath-classifier',
    author='Aleksandr Tereshchenko',
    author_email='aleksandr.tereshch@gmail.com',
    license='MIT',
    packages=['cyclepath_classifier'],
    install_requires=[],
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 4 - Beta',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3.8',
    ]
)
