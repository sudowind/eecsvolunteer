# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-14 06:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('genius', '0003_activity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
