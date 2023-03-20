from django.shortcuts import render, redirect, get_object_or_404
from products.models import Names, Products
from django.views.decorators.http import require_POST
from order.forms import CartAddForm
from order.cart import Cart
from customer.forms import CustomerCreatedForm
from .models import Order
from decimal import Decimal
from .tasks import order_create


def wishlist_page(request):
    category = Names.objects.filter(type="C").prefetch_related("groups")
    return render(request, "wishlist.html", {"names": category})


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Products, id=product_id)
    form = CartAddForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product, quantity=cd["quantity"], update_quantity=cd["update"])
    return redirect("cart_page")


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Products, id=product_id)
    cart.remove(product)
    return redirect("cart_page")


def cart_page(request):
    category = Names.objects.filter(type="C").prefetch_related("groups")
    cart = Cart(request)
    for el in cart:
        el["update_quantity_form"] = CartAddForm(
            initial={"quantity": el["quantity"], "update": True}
        )

    return render(request, "cart.html", {"names": category, "cart": cart})


def checkout_page(request):
    category = Names.objects.filter(type="C").prefetch_related("groups")
    cart = Cart(request)
    if request.method == "POST":
        form = CustomerCreatedForm(request.POST)
        if form.is_valid():
            customer = form.save()
            comment = form.cleaned_data["comment_to_order"]

            for item in cart:
                Order.objects.create(
                    customer=customer,
                    product=item["products"],
                    price=(Decimal(item["price"])),
                    quantity=item["quantity"],
                )
            cart.clear()  # очистка корзины
            order_create.delay(customer.id, comment)
            return redirect("home_page")
    else:
        form = CustomerCreatedForm()
    return render(
        request, "checkout.html", {"names": category, "cart": cart, "form": form}
    )
