from django.db import models
from django.urls import reverse

class Manufacturer(models.Model):
    id = models.BigAutoField(primary_key=True)
    name_man = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name_man
    
    class Meta:
        db_table = 'manufacturer'

class Group(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    manufacturer = models.ManyToManyField(Manufacturer)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'group'



class Names(models.Model):
    id = models.BigAutoField(primary_key=True)
    value = models.CharField(max_length=100)
    type = models.CharField(max_length=3)
    c_g = models.BigIntegerField(null=True)
    groups = models.ManyToManyField(Group)
    #slug = models.SlugField(max_length=100,unique=True)

    def __str__(self):
        return self.value
    

    class Meta:
    #    managed = False
        db_table = 'names'

class Image(models.Model):
    id = models.BigAutoField(primary_key=True)
    img_file_path = models.ImageField(upload_to="image/%Y/%m/%d/")

    class Meta:
    #    managed = False
        db_table = 'image'


class Products(models.Model):
    id = models.BigAutoField(primary_key=True)
    product_name = models.CharField(max_length=64)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    amount = models.IntegerField(blank=True, null=True)  # add def validators if amount < 0 ValidationError !!!!
    category = models.ForeignKey(Names, models.DO_NOTHING, related_name='category_id')
    group = models.ForeignKey(Group, models.DO_NOTHING, related_name='group_id')
    manufacturer = models.ForeignKey(Manufacturer, models.DO_NOTHING, related_name='manufacturer_id')
    model = models.ForeignKey(Names, models.DO_NOTHING, related_name='model_id')
    images = models.ManyToManyField(Image)

    def __str__(self):
        return self.product_name

    
    class Meta:
    #    managed = False
        db_table = 'products'


               
# Create your models here.
