# Generated by Django 4.1.6 on 2023-05-06 03:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_cart'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Cart',
        ),
    ]
