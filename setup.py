#!/usr/bin/env python

from setuptools import setup, find_packages
import os

try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except (IOError, ImportError):
    long_description = ''



setup(
    name='py-security-code',
    version='0.3',
    description='Security Code(equtity, option, bond etc..) of all Exchanges',
    long_description=long_description,
    author='RainX<Jing Xu>',
    author_email='i@rainx.cc',
    url='https://github.com/rainx/py_security_code',
    packages=find_packages(),
    install_requires=[
            #'click',
            #'pandas',
            'six',
            'pytz',
            'PyYAML',
            'enum34',
    ],
    package_data={
        '': ['*.yml'],
    },
    entry_points={
          'console_scripts': [
          ]
      },
    )

