# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-11-27 03:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rbvc', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='permission',
            name='icon',
            field=models.CharField(blank=True, max_length=24, null=True),
        ),
        migrations.AddField(
            model_name='permission',
            name='is_menu',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='role',
            name='permissions',
            field=models.ManyToManyField(blank=True, null=True, to='rbvc.Permission'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='roles',
            field=models.ManyToManyField(blank=True, null=True, to='rbvc.Role'),
        ),
    ]