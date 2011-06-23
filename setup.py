import os
from setuptools import setup, find_packages

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "Django Maintenance",
    version = "0.0.2",
    author = "Andrew Carter, Jamie Curle",
    author_email = "andrewjcarter@gmail.com, me@jamiecurle.com",
    description = ("Django middleware that allows you to perform maintenance on your application "),
    license = "BSD",
    url = "https://github.com/tiemonster/django-maintenance",
    packages=find_packages(),
    long_description=read('README.md'),
)