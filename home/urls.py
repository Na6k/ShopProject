from django.urls import path
from home import views
from django.shortcuts import redirect


urlpatterns = [
    path('', lambda request : redirect('home_page')),
    path('home/', views.home_page, name='home_page'),
    path('contacts/', views.contacts_page, name='contacts_page'),
    path('about/', views.about_page, name='about_page'),
    path('404/', views.pageNotFound, name='pageNotFound')     
]
