from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.registerpage, name="register"),
    path('login/', views.loginpage, name="login"),
    path('logout/', views.logoutpage, name="logout"),
    path('home/', views.homepage, name="home"),
]