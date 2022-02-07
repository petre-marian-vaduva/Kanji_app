from django.contrib import admin
from infrastructure.models import Instance, Server

class InstanceAdmin(admin.ModelAdmin):
    list_display = ('instance_name', 'description', 'status')
    list_filter = ('instance_name', )


class ServerAdmin(admin.ModelAdmin):
    list_display = ('instance_name', 'alias_name', 'server_name', 'ip_address', 'description', 'role')
    list_filter = ('instance_name', )


admin.site.register(Instance, InstanceAdmin)
admin.site.register(Server, ServerAdmin)