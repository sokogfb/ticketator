# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-02-01 20:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20170124_1845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='logo',
            field=models.FileField(upload_to='logo/'),
        ),
    ]
