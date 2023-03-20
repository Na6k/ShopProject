from django.shortcuts import render
from .models import Names, Products, Group, Manufacturer, Image
from order.forms import CartAddForm


def group_page(request, value):
    category = Names.objects.filter(type="C").prefetch_related("groups")
    group = Names.objects.filter(value=value).prefetch_related("groups")
    context = {"names": category, "current": value, "group": group}
    return render(request, "group.html", context=context)


def manufacturer_page(request, value, name):
    category = Names.objects.filter(type="C").prefetch_related("groups")
    grou = Group.objects.filter(name=name).prefetch_related("manufacturer")
    context = {"grou": grou, "current": name, "value": value, "names": category}
    return render(request, "manufacturer.html", context=context)


def products_page(request, value, name, manufacturer):
    category = Names.objects.filter(type="C").prefetch_related("groups")
    c_id = Names.objects.filter(value=value).values("id")
    g_id = Group.objects.filter(name=name).values("id")
    m_id = Manufacturer.objects.filter(name_man=manufacturer).values("id")
    product = Products.objects.filter(
        category_id=c_id[0]["id"], group_id=g_id[0]["id"], manufacturer_id=m_id[0]["id"]
    )
    cart_form = CartAddForm()
    print(product)
    context = {
        "product": product,
        "value": value,
        "name": name,
        "manufacturer": manufacturer,
        "names": category,
        "cart_form": cart_form,
    }

    return render(request, "products.html", context=context)


def product_page(request, name_gr, prod_name):
    category = Names.objects.filter(type="C").prefetch_related("groups")
    product = Group.objects.filter(name=name_gr).values("id")
    about_prod = Products.objects.filter(
        product_name=prod_name, group_id=product[0]["id"]
    ).select_related("category", "group", "manufacturer")
    img = Image.objects.filter(products=about_prod[0])
    print(img)
    try:
        img_active = img[0]
    except IndexError:
        img_active = None

    cart_form = CartAddForm()
    context = {
        "names": category,
        "prod_name": prod_name,
        "about_prod": about_prod,
        "name_gr": name_gr,
        "cart_form": cart_form,
        "image": img,
        "img_active": img_active,
    }
    return render(request, "product.html", context=context)


# Create your views here.
