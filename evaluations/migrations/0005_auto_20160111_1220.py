# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-11 11:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('evaluations', '0004_auto_20160111_0954'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rating',
            old_name='date rated',
            new_name='date_rated',
        ),
    ]
