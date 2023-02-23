from django.shortcuts import render, redirect
from products.models import Names, Group


def home_page(request):
    a = (
        Names.objects
        .filter(type = "C")
        .prefetch_related('groups')
        )
    

    return render(request, 'home.html', {'names' : a})


def contacts_page(request):
    print(request.GET)
    return render(request, 'contacts.html')


def about_page(request):
    print(request.GET)
    return render(request, 'about.html')


def pageNotFound(request, exception):
    return render(request, '404.html')
# Create your views here.
