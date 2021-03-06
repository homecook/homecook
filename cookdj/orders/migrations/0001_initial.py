# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-20 01:14
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        ('meals', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('order_portions', models.IntegerField()),
                ('order_reviewed', models.BooleanField(default=False)),
                ('order_filled', models.BooleanField(default=False)),
                ('order_rated', models.BooleanField(default=False)),
                ('order_total', models.DecimalField(decimal_places=2, max_digits=5)),
                ('order_payment_received', models.BooleanField(default=False)),
                ('order_creation_datetime', models.DateTimeField(default=datetime.datetime(2015, 12, 20, 1, 14, 50, 90436, tzinfo=utc))),
                ('order_modification_datetime', models.DateTimeField(default=datetime.datetime(2015, 12, 20, 1, 14, 50, 90480, tzinfo=utc))),
                ('order_meal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meals.Meal')),
                ('order_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.User')),
            ],
        ),
    ]
