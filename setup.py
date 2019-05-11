# -*- coding: utf-8 -*-

# Learn more: https://github.com/RyanJarv/setup.py

from setuptools import setup, find_packages

with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='orgmanager',
    version='0.1.0',
    description='AWS Organizations manager',
    long_description=readme,
    author='Ryan Gerstenkorn',
    author_email='ryan_gerstenkorn@fastmail.fm',
    url='https://github.com/RyanJarv/orgmanager',
    license=license,

    package_dir={"": "orgmanager"},
    packages=setuptools.find_packages(where="orgmanager"),

    install_requires = [
        'boto3',
        'tabulate',
    ],
    python_requires=">=3.6",

    classifiers=[
        "Development Status :: 4 - Beta",

        "Intended Audience :: Developers",

        "License :: OSI Approved :: Apache Software License",

        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",

        "Topic :: Software Development :: Code Generators",
        "Topic :: Utilities",

        "Typing :: Typed",
    ],
)

