from django.urls import re_path, path
from applications import views


urlpatterns = [
    re_path(r'^requestlorappupgrade/$',views.requestlorappupgradeView,name='requestlorappupgrade'),
    re_path(r'^requestipmappupgrade/$',views.requestipmappupgradeView,name='requestipmappupgrade'),
    path('<version>/', views.all_versions, name='version'),
    # path('', views.test, name='test')
]
