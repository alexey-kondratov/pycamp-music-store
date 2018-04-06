
# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-04-05 08:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_appuser_location_updated'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentMethod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='appuser',
            name='balance',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='appuser',
            name='default_method',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='default_method', to='users.PaymentMethod'),
        ),
        migrations.AddField(
            model_name='appuser',
            name='methods_used',
            field=models.ManyToManyField(related_name='methods_used', to='users.PaymentMethod'),
        ),
]
