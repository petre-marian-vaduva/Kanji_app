from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<slug>/', views.level, name='level'),
    path('kanji_detail/<slug>/', views.kanji_detail, name='kanji_detail'),
    path('update/<slug>', views.update, name='update'),
    path('delete/<slug>', views.delete, name='delete')
]