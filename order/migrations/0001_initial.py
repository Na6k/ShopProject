# Generated by Django 4.1.4 on 2023-03-09 08:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("products", "0008_alter_products_group_alter_products_manufacturer"),
        ("customer", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="PaymentType",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                (
                    "payment_type",
                    models.CharField(
                        choices=[("M", "Наличные"), ("C", "Карта")],
                        default="M",
                        max_length=1,
                    ),
                ),
            ],
            options={
                "db_table": "payment_type",
            },
        ),
        migrations.CreateModel(
            name="Order",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("quantity", models.PositiveIntegerField(default=1)),
                (
                    "delivery_type",
                    models.CharField(
                        choices=[
                            ("B", "Белпочта"),
                            ("E", "Европочта"),
                            ("S", "СДЕК"),
                            ("P", "Самовывоз"),
                        ],
                        default="B",
                        max_length=1,
                    ),
                ),
                (
                    "customer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="customer_id",
                        to="customer.customer",
                    ),
                ),
                (
                    "payment_type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="payment_type_id",
                        to="order.paymenttype",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="product_id",
                        to="products.products",
                    ),
                ),
            ],
        ),
    ]
