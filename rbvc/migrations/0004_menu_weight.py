# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-11-28 09:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rbvc', '0003_auto_20181128_1009'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='weight',
            field=models.PositiveIntegerField(default=50, verbose_name='菜单权重'),
        ),
    ]