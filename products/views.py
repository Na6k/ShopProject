from django.shortcuts import render
from .models import Names, Products


def group_page(request):
    gr = Names.objects.filter(id__gte = 16, id__lte = 19)
    return render(request, 'shop.html')


def manufacturer_page(request):
    return render(request, 'manufacturer.html',)


def products_page(request):
    mikado = Products.objects.filter(category_id = 1, group_id = 16, manufacturer_id = 95)
    

    return render(request, 'products.html', {'mikado': mikado})


def product_page(request):
    return render(request, 'product.html')
# Create your views here.
