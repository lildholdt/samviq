# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-11 08:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evaluations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='observer',
            name='evaluation ended',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='observer',
            name='evaluation started',
            field=models.DateTimeField(null=True),
        ),
    ]
