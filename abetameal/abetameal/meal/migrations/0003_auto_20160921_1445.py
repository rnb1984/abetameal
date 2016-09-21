# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-21 13:45
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meal', '0002_meal_ingrs'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meal',
            name='ingredients',
        ),
        migrations.AlterField(
            model_name='meal',
            name='ingrs',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), blank=True, size=None),
        ),
    ]
