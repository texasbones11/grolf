# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-08-02 14:26
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.date.today)),
            ],
            options={
                'verbose_name_plural': 'Events',
            },
        ),
        migrations.CreateModel(
            name='GolfCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.CharField(max_length=40)),
                ('hole1par', models.PositiveSmallIntegerField()),
                ('hole2par', models.PositiveSmallIntegerField()),
                ('hole3par', models.PositiveSmallIntegerField()),
                ('hole4par', models.PositiveSmallIntegerField()),
                ('hole5par', models.PositiveSmallIntegerField()),
                ('hole6par', models.PositiveSmallIntegerField()),
                ('hole7par', models.PositiveSmallIntegerField()),
                ('hole8par', models.PositiveSmallIntegerField()),
                ('hole9par', models.PositiveSmallIntegerField()),
                ('hole1handicap', models.PositiveSmallIntegerField()),
                ('hole2handicap', models.PositiveSmallIntegerField()),
                ('hole3handicap', models.PositiveSmallIntegerField()),
                ('hole4handicap', models.PositiveSmallIntegerField()),
                ('hole5handicap', models.PositiveSmallIntegerField()),
                ('hole6handicap', models.PositiveSmallIntegerField()),
                ('hole7handicap', models.PositiveSmallIntegerField()),
                ('hole8handicap', models.PositiveSmallIntegerField()),
                ('hole9handicap', models.PositiveSmallIntegerField()),
            ],
            options={
                'verbose_name_plural': 'Golf Courses',
            },
        ),
        migrations.CreateModel(
            name='Leaderboard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hole1score', models.SmallIntegerField()),
                ('hole2score', models.SmallIntegerField()),
                ('hole3score', models.SmallIntegerField()),
                ('hole4score', models.SmallIntegerField()),
                ('hole5score', models.SmallIntegerField()),
                ('hole6score', models.SmallIntegerField()),
                ('hole7score', models.SmallIntegerField()),
                ('hole8score', models.SmallIntegerField()),
                ('hole9score', models.SmallIntegerField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.GolfCourse')),
            ],
            options={
                'verbose_name_plural': 'Leaderboards',
            },
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('handicap', models.FloatField()),
                ('email', models.EmailField(max_length=254)),
            ],
            options={
                'verbose_name_plural': 'Players',
            },
        ),
        migrations.CreateModel(
            name='Tee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teename', models.CharField(max_length=40)),
                ('teeslope', models.FloatField()),
                ('teerating', models.FloatField()),
                ('teecolor', models.CharField(max_length=10)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.GolfCourse')),
            ],
            options={
                'verbose_name_plural': 'Tees',
            },
        ),
        migrations.AddField(
            model_name='player',
            name='teebox',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='events.Tee'),
        ),
        migrations.AddField(
            model_name='leaderboard',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.Player'),
        ),
        migrations.AddField(
            model_name='leaderboard',
            name='tee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.Tee'),
        ),
        migrations.AddField(
            model_name='events',
            name='title',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.GolfCourse'),
        ),
    ]
