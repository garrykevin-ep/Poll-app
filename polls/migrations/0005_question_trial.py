# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-06 09:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_remove_choice_answer'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='trial',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
