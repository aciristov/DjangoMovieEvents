# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-17 13:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('filmskinastani', '0004_auto_20170717_1300'),
    ]

    operations = [
        migrations.AddField(
            model_name='award',
            name='actors',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='filmskinastani.Actor'),
        ),
    ]
