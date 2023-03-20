from django.contrib import admin
from .models import Products, Group, Manufacturer, Image, Names


@admin.register(Names)
class NamesAdmin(admin.ModelAdmin):
    list_display = ["value", "type", "img"]


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ["name"]


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ["name_man"]


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ["img_file_path"]


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ["product_name", "description", "price", "amount"]


# Register your models here.
