from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('category/', views.category, name="category"),
    path('category/category_list/<category_key>', views.category_list, name='category_list'),
]
