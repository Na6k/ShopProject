# Generated by Django 4.1.7 on 2023-03-21 14:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("order", "0002_alter_order_payment_type_alter_order_table"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="delivery_type",
            field=models.CharField(max_length=10),
        ),
    ]