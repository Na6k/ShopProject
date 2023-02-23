from django.urls import path
from django.shortcuts import redirect
from order import views


urlpatterns = [
    path('', lambda request:redirect('home_page')),
    path('wishlist/', views.wishlist_page, name='wishlist_page'),
    path('bascket/', views.bascket_page, name='bascket_page'),
    path('checkout/', views.checkout_page, name='checkout_page'),
]
