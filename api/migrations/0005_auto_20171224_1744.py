# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-24 14:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_piar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='piar',
            name='poster',
            field=models.ImageField(blank=True, null=True, upload_to='files/media/posters/'),
        ),
    ]