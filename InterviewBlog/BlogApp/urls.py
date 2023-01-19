from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="BlogHome"),
    path('login/', views.login, name="BlogAccount"),

]