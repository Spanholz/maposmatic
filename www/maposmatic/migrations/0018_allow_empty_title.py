# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2020-02-23 11:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maposmatic', '0017_uploadfile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maprenderingjob',
            name='maptitle',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
