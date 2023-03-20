from django.urls import path
from django.shortcuts import redirect
from products import views


urlpatterns = [
    path(" ", lambda request: redirect("home_page")),
    path("group/<str:value>", views.group_page, name="group_page"),
    path(
        "products/<str:value>/<str:name>/<str:manufacturer>",
        views.products_page,
        name="products_page",
    ),
    path(
        "manufacturer/<str:value>/<str:name>",
        views.manufacturer_page,
        name="manufacturer_page",
    ),
    path(
        "product/<str:name_gr>/<str:prod_name>", views.product_page, name="product_page"
    ),
]
