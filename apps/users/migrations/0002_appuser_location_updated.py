# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-04-03 03:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='appuser',
            name='location_updated',
            field=models.DateTimeField(blank=True, editable=False, null=True),
        ),
]
