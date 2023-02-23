from django.urls import path
from django.shortcuts import redirect
from products import views

urlpatterns = [
    path(' ', lambda request : redirect('home_page')),
    path('shop/', views.group_page, name='group_page'),
    path('products/', views.products_page, name='products_page'),
    path('manufacturer/', views.manufacturer_page, name='manufacturer_page'),
    path('product/', views.product_page, name='product_page')
]
