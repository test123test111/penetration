# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-08 06:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nmaper', '0009_auto_20160108_0613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nmapscan',
            name='email_text',
            field=models.CharField(max_length=8),
        ),
        migrations.AlterField(
            model_name='nmapscan',
            name='status_text',
            field=models.CharField(choices=[('waiting', 'Waiting'), ('running', 'Running'), ('finished', 'Finished')], max_length=16),
        ),
    ]
