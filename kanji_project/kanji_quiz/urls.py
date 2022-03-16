from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.search, name='search'),
    path('', views.index, name='index'),
    path('kanji_detail/<slug>/', views.kanji_detail, name='kanji_detail'),
    path('update/<slug>', views.update, name='update'),
    path('delete/<slug>', views.delete, name='delete'),
    path('<slug>/', views.level, name='level'),   
]