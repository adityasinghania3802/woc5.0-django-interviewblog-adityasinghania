from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name="index"),
    path('register/', views.registerpage, name="register"),
    path('login/', views.loginpage, name="login"),
    path('logout/', views.logoutpage, name="logout"),
    path('home/', views.homepage, name="home"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('addpost/', views.addpost, name="addpost"),
    path('viewpost/<int:pid>', views.viewpost, name="viewpost")

]