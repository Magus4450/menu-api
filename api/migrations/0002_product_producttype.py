# Generated by Django 4.1 on 2022-09-03 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='productType',
            field=models.CharField(choices=[('VEG', 'VEG'), ('NON_VEG', 'NON_VEG'), ('CONTAINS_EGG', 'CONTAINS_EGG')], default=('VEG', 'VEG'), max_length=12),
        ),
    ]
