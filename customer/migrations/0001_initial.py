# Generated by Django 4.1.4 on 2023-02-20 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(blank=True, max_length=100, null=True)),
                ('phone', models.BigIntegerField()),
                ('email', models.CharField(max_length=100, unique=True)),
                ('contry', models.CharField(default='Belarus', max_length=100)),
                ('town', models.CharField(max_length=100)),
                ('street', models.CharField(max_length=100)),
                ('post_code', models.BigIntegerField()),
            ],
            options={
                'db_table': 'customer',
            },
        ),
    ]
