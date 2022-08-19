# Generated by Django 4.1 on 2022-08-19 14:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
                ('slug', models.SlugField(max_length=225)),
                ('imageUrl', models.TextField(default='\\media\\image\\test.jpg')),
                ('status', models.CharField(choices=[('ACTIVE', 'ACTIVE'), ('PENDING', 'PENDING'), ('DELETED', 'DELETED')], max_length=7)),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
                ('slug', models.SlugField(max_length=225)),
                ('location', models.CharField(max_length=225)),
                ('imageUrl', models.TextField(default='\\media\\image\\test.jpg')),
                ('status', models.CharField(choices=[('ACTIVE', 'ACTIVE'), ('PENDING', 'PENDING'), ('DELETED', 'DELETED')], max_length=7)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField(default='\\media\\image\\test.jpg', max_length=225)),
                ('imageUrl', models.TextField()),
                ('status', models.CharField(choices=[('ACTIVE', 'ACTIVE'), ('PENDING', 'PENDING'), ('DELETED', 'DELETED')], max_length=7)),
                ('categoryId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.category')),
                ('restaurantId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.restaurant')),
            ],
        ),
        migrations.AddField(
            model_name='category',
            name='restaurantId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.restaurant'),
        ),
    ]
