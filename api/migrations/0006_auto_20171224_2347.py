# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-24 20:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20171224_1744'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='categories',
            field=models.ManyToManyField(to='api.Category'),
        ),
        migrations.AlterField(
            model_name='piar',
            name='poster',
            field=models.ImageField(blank=True, null=True, upload_to='posters/'),
        ),
    ]
