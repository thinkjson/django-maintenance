from django.contrib import admin
from maintenance.models import MaintenanceMessage

class MaintenanceMessageAdmin(admin.ModelAdmin):
    pass

admin.site.register(MaintenanceMessage, MaintenanceMessageAdmin)
