# Generated by Django 5.0 on 2023-12-12 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_product_product_image_backside_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='shopname',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AlterField(
            model_name='product',
            name='upload_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]