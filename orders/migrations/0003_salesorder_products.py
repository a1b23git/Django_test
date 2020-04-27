# Generated by Django 3.0.5 on 2020-04-26 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
        ('orders', '0002_salesorder_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='salesorder',
            name='products',
            field=models.ManyToManyField(to='products.Product'),
        ),
    ]