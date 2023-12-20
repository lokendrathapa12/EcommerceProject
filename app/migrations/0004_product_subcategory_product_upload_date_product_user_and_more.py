# Generated by Django 5.0 on 2023-12-12 05:29

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_rename_product_image_product_product_image_backside_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='subcategory',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AddField(
            model_name='product',
            name='upload_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='product',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('TE', 'Tools And Equipment'), ('OF', 'Office furniture'), ('AC', 'Art And Craft'), ('BF', 'Boys Fashion'), ('GF', 'Girls Fashion'), ('MF', 'Men Fashion'), ('WF', 'Women Fashion'), ('B', 'Baby'), ('E', 'Electronics'), ('BP', 'Beauty And Personal Care'), ('SO', 'Sports And Outdoors:'), ('TG', 'Toys And Games'), ('BS', 'Books And Stationry'), ('PS', 'Pet Suppliers'), ('AC', 'Art And Craft'), ('DP', 'Digital Product'), ('FB', 'Food And Beverage'), ('AM', 'Automotive'), ('KA', 'kitchen And Appliances'), ('G', 'Groceries')], default='Mobile', max_length=3),
        ),
    ]
