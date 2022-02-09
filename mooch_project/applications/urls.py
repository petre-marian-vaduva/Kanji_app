from django.conf.urls import include
from django.urls import re_path 
from applications import views


urlpatterns = [
    re_path(r'^requestlorappupgrade/$',views.requestlorappupgradeView,name='requestlorappupgrade'),
    re_path(r'^requestipmappupgrade/$',views.requestipmappupgradeView,name='requestipmappupgrade'),
]
