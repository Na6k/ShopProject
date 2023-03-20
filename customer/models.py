from django.db import models


class Customer(models.Model):
    id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=25)  # Validation
    email = models.EmailField()  # Unique ?????
    contry = models.CharField(max_length=100, default="Belarus")
    region = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    post_code = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)

    class Meta:
        # managed = False
        db_table = "customer"

    def __str__(self):
        return "Customer {}".format(self.id)

    def get_full_cost(self):
        return sum(item.get_cost() for item in self.items.all())


# Create your models here.
