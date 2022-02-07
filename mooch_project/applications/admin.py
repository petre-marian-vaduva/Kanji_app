from django.contrib import admin
from applications.models import ipm_appversions, lor_appversions


class lor_appversionsAdmin(admin.ModelAdmin):
    list_display = ('app_version','app_version_hier','status','description')
    list_filter = ['status',]

class ipm_appversionsAdmin(admin.ModelAdmin):
    list_display = ('app_version','app_version_hier','status','description')
    list_filter = ['status',]

admin.site.register(lor_appversions, lor_appversionsAdmin)
admin.site.register(ipm_appversions, ipm_appversionsAdmin)
