# Generated by Django 5.0 on 2023-12-19 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_orderedplaced_product_owner_orderedplaced_shopname'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='owner_email',
            field=models.EmailField(default='', max_length=150),
        ),
    ]
