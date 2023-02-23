from django.db import models



class Customer(models.Model):
    id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    phone = models.BigIntegerField() # Validation
    email = models.CharField(unique=True, max_length=100) # Unique ?????
    contry = models.CharField(max_length=100, default="Belarus")
    town = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    post_code = models.BigIntegerField() 

    class Meta:
        #managed = False
        db_table = 'customer'
# Create your models here.
