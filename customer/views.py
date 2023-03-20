from django.shortcuts import render
from products.models import Names


def register_page(request):
    category = Names.objects.filter(type="C")
    context = {"names": category}
    return render(request, "register.html", context=context)


def login_page(request):
    category = Names.objects.filter(type="C")
    context = {"names": category}
    return render(request, "login.html", context=context)


def password_page(request):
    category = Names.objects.filter(type="C")
    context = {"names": category}
    return render(request, "forgot_password.html", context=context)


# Create your views here.
