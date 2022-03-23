from django.conf.urls import include
from django.urls import re_path, path
from infrastructure import views

urlpatterns = [
    re_path(r'^ServersALL_JSON/(?P<instance_name>\S+)/$' , views.ajax_admin_getall_machines_for_instance, name='instance_name'),
    path('', views.infrastructure_home, name='infrastructure_home'),
    path('<instance>/', views.instance_view, name='instance_view')
]




