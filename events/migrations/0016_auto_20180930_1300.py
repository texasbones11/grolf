# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-09-30 13:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0015_events_netteamscoring'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leaderboard',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.Handicap'),
        ),
    ]
