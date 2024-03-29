# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-07 11:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cost_Product',
            fields=[
                ('id_cost', models.AutoField(primary_key=True, serialize=False)),
                ('created', models.DateTimeField()),
                ('dateend', models.DateTimeField()),
                ('value', models.FloatField(default=0)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cost_product', to='product.Product')),
            ],
        ),
    ]
