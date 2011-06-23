from setuptools import setup, find_packages


setup(
    name = "Django Maintenance",
    packages = ['maintenance',],
    package_data = {
         'maintenance': [
                 'templates/*.html',
             ],
     },
    version = "0.0.2",
    author = "Andrew Carter, Jamie Curle",
    author_email = "andrewjcarter@gmail.com, me@jamiecurle.com",
    description = ("Django middleware that allows you to perform maintenance on your application "),
    license = "BSD",
    url = "https://github.com/tiemonster/django-maintenance",

)