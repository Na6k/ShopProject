from django.urls import path
from django.shortcuts import redirect
from customer import views


urlpatterns = [
    path("", lambda request: redirect("home_page")),
    path("register/", views.register_page, name="register_page"),
    path("login/", views.login_page, name="login_page"),
    path("forgot_password/", views.password_page, name="password_page"),
]
