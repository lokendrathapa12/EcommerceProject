# Generated by Django 5.0 on 2023-12-17 05:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0003_rename_slectproduct_selectproduct'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='selectproduct',
            name='vendor',
        ),
    ]
