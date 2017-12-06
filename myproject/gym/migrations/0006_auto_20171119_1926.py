# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-11-19 17:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0005_set'),
    ]

    operations = [
        migrations.AlterField(
            model_name='set',
            name='workout',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sets', to='gym.Workout'),
        ),
    ]