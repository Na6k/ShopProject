# Generated by Django 4.1.4 on 2023-02-20 08:52

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="products",
            old_name="category_id",
            new_name="category",
        ),
        migrations.RenameField(
            model_name="products",
            old_name="group_id",
            new_name="group",
        ),
        migrations.RenameField(
            model_name="products",
            old_name="manufacturer_id",
            new_name="manufacturer",
        ),
        migrations.RenameField(
            model_name="products",
            old_name="model_id",
            new_name="model",
        ),
    ]