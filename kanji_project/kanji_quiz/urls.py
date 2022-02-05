from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<slug>/', views.level, name='level'),
    path('<slug>/', views.kanji_detail, name='kanji_detail')
]