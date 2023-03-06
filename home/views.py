from django.shortcuts import render, redirect
from products.models import Names, Group, Manufacturer


def home_page(request):
    category = (
        Names.objects
        .filter(type = "C")
        .prefetch_related('groups')
        )
    return render(request, 'home.html', {'names' : category})


def contacts_page(request):
    print(request.GET)
    return render(request, 'contacts.html')


def about_page(request):
    category = (
        Names.objects
        .filter(type = "C")
        .prefetch_related('groups')
        )
    print(request.GET)
    return render(request, 'about.html', {'names': category})


def pageNotFound(request, exception):
    return render(request, '404.html')
# Create your views here.
