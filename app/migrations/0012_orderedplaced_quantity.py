# Generated by Django 5.0 on 2023-12-18 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_alter_customers_phone_alter_customers_provience'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderedplaced',
            name='quantity',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
