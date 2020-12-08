from django.contrib import admin
from django.urls import path, include, re_path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('category/', views.category, name="category"),
    path('category/category_list/<category_key>', views.category_list, name='category_list'),
    path('format/', views.format, name="format"),
    path('format/format_list/<format_key>', views.format_list, name='format_list'),
]
