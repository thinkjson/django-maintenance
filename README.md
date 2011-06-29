Django middleware that allows you to perform maintenance on your application without having to restart your server. 

Other maintenance mode solutions for Django rely on a settings.py change, which in turn needs a server restart (touching the wsgi file, or even restarting Apache). This application allows you to control maintenance mode from the Django admin, customizing the message available to the end user, and for how long the application will be down. 

You can even schedule future maintenance windows without having to worry about manually taking down the application when maintenance becomes necessary. 

Be aware however that if enabled, every request will incur one extra database query unless you also enable MAINTENANCE_CACHE_MESSAGES (see below).

## Setup

To set this up, add `maintenance` to your INSTALLED_APPS and `maintenance.middleware.MaintenanceMiddleware` to the bottom of your MIDDLEWARE_CLASSES settings, and then run `manage.py syncdb`.

## Configuration

### MAINTENANCE_DISABLE_FOR_SUPERUSER

If set to True then superusers will be able to access the site as normal and the middleware will have no effect. Defaults to False.

### MAINTENANCE_CACHE_MESSAGES

If set to True, maintenance messages are cached with Django's cache framework, avoiding the extra database query per request. The cache is invalidated every time a new message is saved. Defaults to False.

### MAINTENANCE_CACHE_SECONDS

Defines the length of time (in seconds) that maintenance messages are cached for, when MAINTENANCE_CACHE_MESSAGES is enabled. Defaults to 3600.