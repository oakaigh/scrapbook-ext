#!/usr/bin/env python3

import setuptools


setuptools.setup(
    name='scrapbook-ext',
    version='0.0.0a',
    description='Extensions for scrapbook',
    python_requires='>=3.6',
    packages=['scrapbook_ext'],
    package_dir={
        '': 'src'
    },
    install_requires=[
        'scrapbook'
    ],
    extras_require={
        'dev': []
    }
)
