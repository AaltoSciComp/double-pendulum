#!/usr/bin/env python

from setuptools import setup

setup(name='double-pendulum',
      version='1.0',
      description='A double pendulum simulator',
      author='Diego Assencio',
      author_email='diego@assencio.com',
      url='https://github.com/AaltoSciComp/double-pendulum',
      install_requires=[
          'numpy',
          'pygame',
      ],
      entry_points={
          'console_scripts' : [
              'double-pendulum=doublependulum:main',
          ]
      },
)
