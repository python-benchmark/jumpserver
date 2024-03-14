# Generated by Django 3.2.14 on 2022-10-27 03:25

import uuid

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('assets', '0101_auto_20220811_1511'),
        ('terminal', '0053_auto_20221009_1755'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='protocol',
            field=models.CharField(db_index=True, default='ssh', max_length=16),
        ),
        migrations.RenameField(
            model_name='session',
            old_name='system_user',
            new_name='account',
        ),
        migrations.RemoveField(
            model_name='session',
            name='system_user_id',
        ),
        migrations.AlterField(
            model_name='session',
            name='account',
            field=models.CharField(db_index=True, max_length=128, verbose_name='Account'),
        ),
        migrations.AddField(
            model_name='session',
            name='comment',
            field=models.TextField(blank=True, null=True, verbose_name='Comment'),
        ),
        migrations.AddField(
            model_name='session',
            name='type',
            field=models.CharField(db_index=True, default='normal', max_length=16),
        ),
    ]
