# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-09-26 20:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0013_auto_20180926_1821'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teamleaderboard',
            name='handicap',
        ),
    ]
