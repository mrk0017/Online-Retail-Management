# Generated by Django 3.0.4 on 2020-03-29 01:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ShoppersPoint', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_date', models.DateTimeField()),
                ('quantity', models.IntegerField(default=1)),
                ('status', models.CharField(default='', max_length=210)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ShoppersPoint.Products')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Cart',
                'verbose_name_plural': 'Cart',
            },
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ShoppersPoint.Products')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Cart',
                'verbose_name_plural': 'Cart',
            },
        ),
        migrations.CreateModel(
            name='Addressbook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('house_number', models.CharField(default='', max_length=250)),
                ('locality', models.CharField(default='', max_length=250)),
                ('region', models.CharField(default='', max_length=250)),
                ('postcode', models.CharField(default='', max_length=250)),
                ('country', models.CharField(default='', max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Address',
                'verbose_name_plural': 'Address',
            },
        ),
    ]
