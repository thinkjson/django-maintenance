from maintenance.models import MaintenanceMessage
from datetime import datetime
from django.template.loader import render_to_string
from django.template import RequestContext
from django.http import HttpResponse
from django.core.urlresolvers import resolve
from django.db.models import Q

class MaintenanceMiddleware(object):
    def process_request(self, request):
        messages = MaintenanceMessage.objects.filter(start_time__lt=datetime.now())\
            .filter(\
            Q(end_time__gte=datetime.now()) | Q(end_time__isnull=True) )
        try:
            view, args, kwargs = resolve(request.path)
        except Exception:
            return None
        if 'django.contrib.admin' not in view.__module__ and messages.count() > 0:
            template = render_to_string('503.html',
            {
                'title': 'Maintenance Mode',
                'messages': messages
            }, context_instance=RequestContext(request))
            return HttpResponse(template, status=503)
        else:
            return None