from django.contrib import admin
from scheduler.models import Runtime

class RuntimeAdmin(admin.ModelAdmin):
    list_display = ('instance_name', 'server_name', 'status', 'application', 'application_version', 'start_datetime', 'end_datetime', 'description')
    list_filter = ('instance_name', )

admin.site.register(Runtime, RuntimeAdmin)
