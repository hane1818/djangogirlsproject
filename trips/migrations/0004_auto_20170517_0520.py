# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-05-17 05:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0003_post_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='contact',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AlterField(
            model_name='post',
            name='photo',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]