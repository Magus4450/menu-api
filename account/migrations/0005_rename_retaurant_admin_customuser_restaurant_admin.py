# Generated by Django 4.1 on 2022-08-30 14:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_customuser_retaurant_admin'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='retaurant_admin',
            new_name='restaurant_admin',
        ),
    ]
