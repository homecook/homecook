# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-13 00:41
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('orders', '0002_auto_20160312_1941'),
        ('meals', '0002_auto_20151219_2014'),
    ]

    operations = [
        migrations.AddField(
            model_name='meal',
            name='meal_subscribers',
            field=models.ManyToManyField(related_name='meals', through='orders.Order', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='meal',
            name='meal_cook',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='meal', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='meal',
            name='meal_creation_datetime',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='meal',
            name='meal_modification_datetime',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='mealrating',
            name='rating_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
