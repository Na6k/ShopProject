from django.urls import path
from django.shortcuts import redirect
from order import views


urlpatterns = [
    path("", lambda request: redirect("home_page")),
    path("wishlist/", views.wishlist_page, name="wishlist_page"),
    path("cart/", views.cart_page, name="cart_page"),
    path("add/<int:product_id>/", views.cart_add, name="cart_add"),
    path("remove/<int:product_id>/", views.cart_remove, name="cart_remove"),
    # path("create/", views.order_create, name='order_create'),
    path("checkout/", views.checkout_page, name="checkout_page"),
]
