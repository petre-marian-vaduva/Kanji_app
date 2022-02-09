from django.conf.urls import include
from django.urls import re_path 
from infrastructure import views

urlpatterns = [
    re_path(r'^ServersALL_JSON/(?P<instance_name>\S+)/$' , views.ajax_admin_getall_machines_for_instance, name='instance_name'),
]
