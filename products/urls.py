from django.urls import path
from django.shortcuts import redirect
from products import views

urlpatterns = [
    path(' ', lambda request : redirect('home_page')),
    #path('group/', views.group_page, name='group_page'),
    path('group/<str:value>', views.group_page, name='group_page'),
    #path('names/<int:names_id>',views.group_page,name="names"),
    path('products/', views.products_page, name='products_page'),
    path('manufacturer/<str:name>', views.manufacturer_page, name='manufacturer_page'),
    path('product/', views.product_page, name='product_page')
]
