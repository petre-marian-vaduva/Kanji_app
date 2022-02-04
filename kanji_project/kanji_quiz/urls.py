from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<slug>', views.level1, name='level1')
]
