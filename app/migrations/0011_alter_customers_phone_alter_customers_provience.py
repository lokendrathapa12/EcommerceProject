# Generated by Django 5.0 on 2023-12-17 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_delete_vendormodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customers',
            name='phone',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='customers',
            name='provience',
            field=models.CharField(choices=[('KP', 'Karnali Provience'), ('BP', 'Bagmati Provience'), ('GP', 'Gandaki Provience'), ('LP', 'Lumbini Pradesh'), ('KO', 'Koshi Pradesh'), ('MP', 'Madesh Pradesh'), ('SP', 'Sudurpashim pradesh')], default='Bagmati Provience', max_length=2),
        ),
    ]
