from django.db import models
from django.urls import reverse


class Manufacturer(models.Model):
    id = models.BigAutoField(primary_key=True)
    name_man = models.CharField(max_length=100)
    img = models.ImageField(upload_to="image/%Y/%m/%d/", null=True)

    def __str__(self):
        return self.name_man

    class Meta:
        db_table = "manufacturer"
        verbose_name = "Производитель"
        verbose_name_plural = "Производители"
        index_together = (("id", "name_man"),)


class Group(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to="image/%Y/%m/%d/", null=True)
    manufacturer = models.ManyToManyField(Manufacturer)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "group"
        verbose_name = "Подкатегория"
        verbose_name_plural = "Подкатегории"
        index_together = (("id", "name"),)


class Names(models.Model):
    id = models.BigAutoField(primary_key=True)
    value = models.CharField(max_length=100)
    type = models.CharField(max_length=3)
    img = models.ImageField(upload_to="image/%Y/%m/%d/", null=True)
    groups = models.ManyToManyField(Group)
    # slug = models.SlugField(max_length=100,unique=True)

    def __str__(self):
        return self.value

    class Meta:
        # managed = False
        db_table = "names"
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        index_together = (("id", "value"),)


class Image(models.Model):
    id = models.BigAutoField(primary_key=True)
    img_file_path = models.ImageField(upload_to="image/%Y/%m/%d/")

    class Meta:
        #    managed = False
        db_table = "image"


class Products(models.Model):
    id = models.BigAutoField(primary_key=True)
    product_name = models.CharField(max_length=64)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    amount = models.IntegerField(
        blank=True, null=True
    )  # add def validators if amount < 0 ValidationError !!!!
    category = models.ForeignKey(Names, models.DO_NOTHING, related_name="category_id")
    group = models.ForeignKey(Group, models.DO_NOTHING, related_name="group_id")
    manufacturer = models.ForeignKey(
        Manufacturer, models.DO_NOTHING, related_name="manufacturer_id"
    )
    img = models.ImageField(upload_to="image/product/%Y", null=True)
    images = models.ManyToManyField(Image)

    def __str__(self):
        return self.product_name

    class Meta:
        #    managed = False
        db_table = "products"
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        index_together = (("id", "product_name"),)


# Create your models here.
