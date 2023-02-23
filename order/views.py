from django.shortcuts import render

def wishlist_page(request):
    return render(request, 'wishlist.html')

def bascket_page(request):
    return render(request, 'bascket.html')

def checkout_page(request):
    return render(request, 'checkout.html')

# Create your views here.
