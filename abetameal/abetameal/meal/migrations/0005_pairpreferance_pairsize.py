# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-24 16:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meal', '0004_preferance_ownertype'),
    ]

    operations = [
        migrations.AddField(
            model_name='pairpreferance',
            name='pairsize',
            field=models.IntegerField(default=0),
        ),
    ]
