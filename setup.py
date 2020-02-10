import os
from setuptools import find_packages, find_namespace_packages, setup


with open(os.path.join(os.path.dirname(__file__), "README.md")) as readme:
    README = readme.read()


# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))


# dynamically compute the version, etc....
author = __import__("dat_utils").__author__
title = __import__("dat_utils").__title__
version = __import__("dat_utils").__version__


install_requires = ["pyjwt~=1.7.1"]


setup(
    name=title,
    version=version,
    author=author,
    url="https://github.com/astrosat/dat-utils",
    description="Data Access Token Utilities",
    long_description=README,
    long_description_content_type="text/markdown",
    install_requires=install_requires,
    packages=find_packages(exclude=["example"]),
    include_package_data=True,
    classifiers=[
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    python_requires=">=3.5",
)
