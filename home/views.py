from django.shortcuts import render, redirect
from products.models import Names
from .forms import ContactForm
from .tasks import get_letter


def home_page(request):
    category = Names.objects.filter(type="C").prefetch_related("groups")
    return render(request, "home.html", {"names": category})


def contacts_page(request):
    category = Names.objects.filter(type="C").prefetch_related("groups")
    contact_form = ContactForm()
    context = {"names": category, "contact_form": contact_form}
    if request.method == "POST":
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            name = contact_form.cleaned_data["name"]
            email = contact_form.cleaned_data["email"]
            subject = contact_form.cleaned_data["subject"]
            company = contact_form.cleaned_data["company"]
            message = contact_form.cleaned_data["message"]
            # send_mail(f'{name}: {subject}',
            #          f"Вам пишет {name} из {company}, по теме: {subject},\n\
            #          сообщение: {message}, обратная связь: {email}",
            #          settings.EMAIL_HOST_USER,
            #          [settings.RECIPIENTS_EMAIL],
            #          fail_silently=False)
            get_letter.delay(name, email, subject, company, message)
            return redirect("home_page")

    return render(request, "contacts.html", context=context)


def about_page(request):
    category = Names.objects.filter(type="C").prefetch_related("groups")
    print(request.GET)
    return render(request, "about.html", {"names": category})


def pageNotFound(request, exception):
    return render(request, "404.html")


def delivery_page(request):
    category = Names.objects.filter(type="C").prefetch_related("groups")
    return render(request, "delivery.html", {"names": category})


# Create your views here.
