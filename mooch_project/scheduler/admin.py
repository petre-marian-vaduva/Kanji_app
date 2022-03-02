from django.contrib import admin
from scheduler.models import Runtime, Jobs, Tasks, Order

class RuntimeAdmin(admin.ModelAdmin):
    list_display = ('instance_name', 'server_name', 'status', 'application', 'application_version', 'start_datetime', 'end_datetime', 'job')
    list_filter = ['instance_name', ]

class JobsAdmin(admin.ModelAdmin):
    list_display = ('job',)

class TasksAdmin(admin.ModelAdmin):
    list_display = ('task',)

class OrderAdmin(admin.ModelAdmin):
    list_display = ('job', 'task')

admin.site.register(Runtime, RuntimeAdmin)
admin.site.register(Jobs, JobsAdmin)
admin.site.register(Tasks, TasksAdmin)
admin.site.register(Order, OrderAdmin)

