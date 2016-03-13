# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-13 02:04
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0003_auto_20160312_1941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meal',
            name='meal_cook',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='meals_cook', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='meal',
            name='meal_subscribers',
            field=models.ManyToManyField(related_name='meals_subscribe', through='orders.Order', to=settings.AUTH_USER_MODEL),
        ),
    ]