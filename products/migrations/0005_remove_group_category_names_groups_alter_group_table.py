# Generated by Django 4.1.4 on 2023-02-23 19:04

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0004_group"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="group",
            name="category",
        ),
        migrations.AddField(
            model_name="names",
            name="groups",
            field=models.ManyToManyField(to="products.group"),
        ),
        migrations.AlterModelTable(
            name="group",
            table="group",
        ),
    ]
