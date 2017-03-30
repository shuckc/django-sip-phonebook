#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

requirements = [
    "django-basic-authentication-decorator"
]

test_requirements = [
    "unittest2==1.1.0"
]

setup(
    name='django-sip-phonebook',
    version='1.0.11',
    description='Django based phonebook for Granstream telephones.',
    long_description='Django based phonebook for Granstream telephones.',
    author='Chris Shucksmith',
    url='https://github.com/shuckc/django-sip-phonebook',
    author_email='chris@shucksmith.co.uk',
    license='MIT',
    include_package_data=True,
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    install_requires=requirements,
    test_suite="tests",
    tests_require=test_requirements,
    classifiers=[
        'Intended Audience :: Developers',
        'Topic :: Software Development',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
)
