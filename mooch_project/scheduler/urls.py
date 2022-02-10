from django.urls import re_path, path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('<slug>/', views.instances, name='instances'),
    
]
