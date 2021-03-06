# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-24 20:22
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('filmskinastani', '0005_award_actors'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='actor',
            name='movies',
        ),
        migrations.RemoveField(
            model_name='award',
            name='actors',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='movies',
        ),
        migrations.RemoveField(
            model_name='producent',
            name='awards',
        ),
        migrations.AddField(
            model_name='actor',
            name='award',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='filmskinastani.Award'),
        ),
        migrations.AddField(
            model_name='award',
            name='festival',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='filmskinastani.Festival'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comment',
            name='movie',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='filmskinastani.Movie'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='movie',
            name='actors',
            field=models.ManyToManyField(to='filmskinastani.Actor'),
        ),
        migrations.AddField(
            model_name='movie',
            name='producent',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='filmskinastani.Producent'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='producent',
            name='award',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='filmskinastani.Award'),
        ),
    ]
