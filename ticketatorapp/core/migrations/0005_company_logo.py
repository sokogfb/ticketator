# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-01-24 14:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_logs_log_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='logo',
            field=models.FileField(default='/logo/tk-tiny.png', upload_to='logo/'),
        ),
    ]