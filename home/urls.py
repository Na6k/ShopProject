from django.urls import path
from home import views
from django.shortcuts import redirect

from products import views as v


urlpatterns = [
    path("", lambda request: redirect("home_page")),
    path("home/", views.home_page, name="home_page"),
    # path('names/<int:names_id>',v.group_page,name="names"),
    path("contacts/", views.contacts_page, name="contacts_page"),
    path("about/", views.about_page, name="about_page"),
    path("404/", views.pageNotFound, name="pageNotFound"),
    path("delivery/", views.delivery_page, name="delivery_page"),
]
