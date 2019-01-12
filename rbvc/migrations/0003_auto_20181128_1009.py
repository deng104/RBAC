# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-11-28 02:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rbvc', '0002_auto_20181127_1152'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=24, unique=True, verbose_name='菜单名称')),
                ('icon', models.CharField(blank=True, max_length=24, null=True)),
            ],
            options={
                'verbose_name': '菜单',
                'verbose_name_plural': '菜单',
            },
        ),
        migrations.RenameField(
            model_name='permission',
            old_name='is_menu',
            new_name='show',
        ),
        migrations.RemoveField(
            model_name='permission',
            name='icon',
        ),
        migrations.AlterField(
            model_name='permission',
            name='title',
            field=models.CharField(max_length=32, verbose_name='标题'),
        ),
        migrations.AddField(
            model_name='permission',
            name='menu',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='rbvc.Menu', verbose_name='所属菜单'),
        ),
    ]
