# Generated by Django 4.1.2 on 2022-10-30 14:06

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
                ('name', models.CharField(max_length=100)),
                ('imageUrl', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.IntegerField()),
                ('imageUrl', models.CharField(max_length=1000)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FlowerShopApp.category')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=12)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('product', models.ManyToManyField(to='FlowerShopApp.product')),
            ],
        ),
    ]
