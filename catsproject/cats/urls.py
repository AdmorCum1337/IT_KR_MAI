from django.urls import path
from . import views

urlpatterns = [
    path('', views.cat_list, name='cat_list'),
    path('create/', views.cat_create, name='cat_create'),
    path('update/<int:pk>/', views.cat_update, name='cat_update'),
    path('delete/<int:pk>/', views.cat_delete, name='cat_delete'),
    path('about', views.about, name='about'),
]