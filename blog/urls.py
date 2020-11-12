from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    
    path('postComment', views.postComment,name="postComment"),
    path('', views.blogHome,name="blogHome"),
    path('<str:slug>/', views.blogPost,name="blogPost"),
    path('signup', views.handleSignUp,name="handleSignUp"),
    path('login', views.handleLogin,name="handleLogin"),
    path('logout', views.handleLogout,name="handleLogout"),
]