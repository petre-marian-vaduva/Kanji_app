from django.urls import re_path, path
from . import views


urlpatterns = [
    path('', views.jobs_home, name='jobs_home'),
    path('<instance_type>/', views.instance, name='instance'),    
]
