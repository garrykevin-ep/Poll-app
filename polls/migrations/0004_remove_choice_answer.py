# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-06 09:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_choice_answer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='answer',
        ),
    ]