from django.urls import path
from django.shortcuts import render, redirect
from blog import views


urlpatterns = [
    path("", lambda request: render("home_page")),
    path("blog/", views.blog_page, name="blog_page"),
    path("single_blog/", views.single_blog_page, name="single_blog_page"),
]
