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
    version = "0.0.3",
    author = "Andrew Carter, Jamie Curle",
    author_email = "andrewjcarter@gmail.com, me@jamiecurle.com",
    description = ("Django middleware that allows you to perform maintenance on your application "),
    license = "BSD",
    url = "https://github.com/tiemonster/django-maintenance",

)