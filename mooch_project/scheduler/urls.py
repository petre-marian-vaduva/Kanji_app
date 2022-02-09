from django.urls import re_path, path
from . import views


urlpatterns = [
    path('<slug>', views.instances, name='instances')
]
