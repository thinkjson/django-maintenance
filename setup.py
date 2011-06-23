#from setuptools import setup, find_packages
from distutils.core import setup

setup(
    name = "django-maintenance",
    package_dir={'django-maintenance': ''},
    packages = ['maintenance',],
    package_data = {
        'maintenance': [
             'templates/*.html',
         ],
    },
    include_package_data=True,
    version = "0.0.3a",
    author = "Mark Cahill",
    description = ("Django middleware that allows you to perform maintenance on your application "),
    license = "BSD",
    url = "https://github.com/tiemonster/django-maintenance",

)