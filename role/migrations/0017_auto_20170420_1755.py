# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-04-20 17:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('role', '0016_remove_assignment_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='target',
            field=models.CharField(max_length=32),
        ),
    ]
