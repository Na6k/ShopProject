from django.shortcuts import render
from .models import Names, Products, Group


def group_page(request, value):
    category = (
        Names.objects
        .filter(type = "C")
        .prefetch_related('groups')
        )
    group = (
        Names.objects
        .filter(value = value)
        .prefetch_related('groups')
        )
    return render(request, 'group.html', {'names': category, 'current': value, 'group': group})


def manufacturer_page(request, value,name):    
    grou = (
        Group.objects
        .filter(name = name)
        .prefetch_related('manufacturer')
        )    
    return render(request, 'manufacturer.html', {'grou':grou, "current": name, 'value': value})


def products_page(request):
    mikado = Products.objects.filter(category_id = 1, group_id = 16, manufacturer_id = 95)
    return render(request, 'products.html', {'mikado': mikado})


def product_page(request):
    return render(request, 'product.html')
# Create your views here.
