from django.contrib import admin
from applications.models import ipm_appversions, lor_appversions


@admin.action(description='Mark selected stories as Draft')
def make_published(self, request,queryset):
    rows_updated=queryset.update(Rep_Status='d')

    if rows_updated == 1:
        message_bit = "1 App version was"
    else:
        message_bit = "%s App versions were" % rows_updated
    self.message_user(request, "%s successfully marked as Draft." % message_bit)
    make_published.short_description = "Mark selected App Versions as Draft"


@admin.action(description='Mark selected stories as Published')
def make_published2(self, request,queryset):
    rows_updated=queryset.update(Rep_Status='p')
    if rows_updated == 1:
        message_bit = "1 App version was"
    else:
        message_bit = "%s App versions were" % rows_updated
    self.message_user(request, "%s successfully marked as Published." % message_bit)
    make_published.short_description = "Mark selected App Versions as Published"


@admin.action(description='Mark selected stories as Withdrawn')
def make_published3(self, request,queryset):
    rows_updated=queryset.update(Rep_Status='w')
    if rows_updated == 1:
        message_bit = "1 App version was"
    else:
        message_bit = "%s App versions were" % rows_updated
    self.message_user(request, "%s successfully marked as Withdrawn." % message_bit)
    make_published.short_description = "Mark selected App Versions as Withdrawn"



class lor_appversionsAdmin(admin.ModelAdmin):
    list_display = ('app_version','app_version_hier','status','description', 'Rep_Status')
    list_filter = ['status',]
    actions = [make_published, make_published2, make_published3]

class ipm_appversionsAdmin(admin.ModelAdmin):
    list_display = ('app_version','app_version_hier','status','description', 'Rep_Status')
    list_filter = ['status',]
    actions = [make_published, make_published2, make_published3]


admin.site.register(lor_appversions, lor_appversionsAdmin)
admin.site.register(ipm_appversions, ipm_appversionsAdmin)
