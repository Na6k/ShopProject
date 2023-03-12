from django.shortcuts import render


def blog_page(request):
    return render(request, "blog.html")


def single_blog_page(request):
    return render(request, "single_blog.html")


# Create your views here.
