# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-10 15:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0014_auto_20171204_1955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='routine',
            name='comments',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='routine',
            name='plan',
            field=models.ManyToManyField(blank=True, to='gym.Plan'),
        ),
        migrations.AlterField(
            model_name='workout',
            name='comments',
            field=models.TextField(blank=True, default=''),
        ),
    ]
