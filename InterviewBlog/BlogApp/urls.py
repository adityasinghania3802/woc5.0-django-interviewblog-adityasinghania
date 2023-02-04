from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.index, name="index"),
    path('register/', views.registerpage, name="register"),
    path('login/', views.loginpage, name="login"),
    path('logout/', views.logoutpage, name="logout"),
    path('home/', views.homepage, name="home"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('addpost/', views.addpost, name="addpost"),
    path('viewpost/<int:pid>', views.viewpost, name="viewpost"),
    path('search/', views.search, name="search"),
    path('bookmarks/<int:pid>', views.bookmarks, name="bookmarks"),
    path('likes/<int:pid>', views.likes, name="likes"),
    path('bookmarks_list/', views.bookmarkslist, name="bookmarkslist"),
    path('myblogs/',views.myblogs, name="myblogs"),
    path('editpost/<int:pid>', views.editpost, name="editpost"),
    path('editpostrecord/<int:pid>',views.editpostrecord,name="editpostrecord"),
    path('deletepost/<int:pid>', views.deletepost, name="deletepost"),
    path('viewpost/<int:pid>/addcomment', views.addcomment, name="addcomment"),
    path('editprofile/',views.editprofile,name="editprofile"),
    path('reset_password/',auth_views.PasswordResetView.as_view(), name="reset_password"),
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),

]