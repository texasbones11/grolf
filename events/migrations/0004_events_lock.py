# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-08-16 19:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_auto_20180807_1847'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='lock',
            field=models.BooleanField(default=False),
        ),
    ]
