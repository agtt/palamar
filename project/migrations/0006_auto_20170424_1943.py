# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-04-24 19:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0005_auto_20170423_0941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='name',
            field=models.CharField(max_length=64, unique=True),
        ),
    ]