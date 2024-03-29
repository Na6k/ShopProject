# Generated by Django 4.1.4 on 2023-02-28 11:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0007_remove_manufacturer_groups_group_manufacturer"),
    ]

    operations = [
        migrations.AlterField(
            model_name="products",
            name="group",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="group_id",
                to="products.group",
            ),
        ),
        migrations.AlterField(
            model_name="products",
            name="manufacturer",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="manufacturer_id",
                to="products.manufacturer",
            ),
        ),
    ]
