from django.db import models
from customer.models import Customer
from products.models import Products


class PaymentType(models.Model):
    PAY_1 = "M"  # payment_type : Money
    PAY_2 = "C"  # payment_type : Card
    PAYMENT_CHOISES = [(PAY_1, "Наличные"), (PAY_2, "Карта")]

    id = models.BigAutoField(primary_key=True)
    payment_type = models.CharField(max_length=1, choices=PAYMENT_CHOISES, default="M")

    class Meta:
        # managed = False
        db_table = "payment_type"


class Order(models.Model):
    # S_1 = "P"  # status : Processing
    # S_2 = "A"  # status : Assembled
    # S_3 = "S"  # status : Sent
    # STATUS_CHOISES = [(S_1, "В обработке"), (S_2, "Собран"), (S_3, "Отправлен")]

    DELIVERY_1 = "B"  # Delivery tupe : BelPost
    DELIVERY_2 = "E"  # Delivery tupe : EuroPost
    DELIVERY_3 = "S"  # Delivery tupe : SDEC
    DELIVERY_4 = "P"  # Delivery tupe : Pickup
    DELIVERY_CHOISES = [
        (DELIVERY_1, "Белпочта"),
        (DELIVERY_2, "Европочта"),
        (DELIVERY_3, "СДЕК"),
        (DELIVERY_4, "Самовывоз"),
    ]

    id = models.BigAutoField(primary_key=True)
    customer = models.ForeignKey(
        Customer, models.DO_NOTHING, related_name="customer_id"
    )
    product = models.ForeignKey(Products, models.DO_NOTHING, related_name="product_id")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
    # status = models.CharField(max_length=1, choices=STATUS_CHOISES, default="P")
    payment_type = models.ForeignKey(
        PaymentType,
        models.DO_NOTHING,
        related_name="payment_type_id",
        null=True,
        blank=True,
    )
    delivery_type = models.CharField(
        max_length=1, choices=DELIVERY_CHOISES, default="B"
    )

    def __str__(self):
        return "Order {}".format(self.id)

    def get_cost(self):
        return self.price * self.quantity

    class Meta:
        db_table = "order"


# Create your models here.
