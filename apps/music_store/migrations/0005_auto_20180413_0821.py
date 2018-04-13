# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-04-13 08:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('music_store', '0004_auto_20180413_0347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boughtalbum',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='purchased', to='music_store.Album', verbose_name='Album'),
        ),
        migrations.AlterField(
            model_name='boughttrack',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='purchased', to='music_store.Track', verbose_name='Track'),
        ),
    ]
