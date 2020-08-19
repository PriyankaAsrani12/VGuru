from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index,name="index"),
    path('<int:id>', views.years, name="year"),
    path('search/', views.search, name='search')
]