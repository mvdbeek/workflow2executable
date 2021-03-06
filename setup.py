#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['Click>=6.0', 'bioblend>=0.14.0','jinja2']

setup_requirements = ['pytest-runner', ]

test_requirements = ['pytest', ]

setup(
    author="Marius van den Beek",
    author_email='m.vandenbeek@gmail.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    description="Turn Galaxy Workflows into standalone scripts.",
    entry_points={
        'console_scripts': [
            'workflow2executable=workflow2executable.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='workflow2executable',
    name='workflow2executable',
    packages=find_packages(include=['workflow2executable']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/mvdbeek/workflow2executable',
    version='0.1.1',
    zip_safe=False,
)
