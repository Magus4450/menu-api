# Generated by Django 4.1 on 2022-08-27 04:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tokenvalidation',
            name='email',
            field=models.EmailField(default='test@test.com', max_length=254, unique=True, verbose_name='Email'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tokenvalidation',
            name='timeTried',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tokenvalidation',
            name='userId',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
