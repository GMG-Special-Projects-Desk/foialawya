# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-12 16:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foias', '0027_auto_20170608_1340'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tag',
            options={'verbose_name': 'Project/Tag', 'verbose_name_plural': 'Projects/Tags'},
        ),
        migrations.AlterField(
            model_name='foia',
            name='tags',
            field=models.ManyToManyField(blank=True, to='foias.Tag', verbose_name='What project(s) is this request a part of?'),
        ),
    ]
