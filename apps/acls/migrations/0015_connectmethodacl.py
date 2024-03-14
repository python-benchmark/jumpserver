# Generated by Django 3.2.17 on 2023-06-06 06:23

import uuid

import django.core.validators
from django.conf import settings
from django.db import migrations, models

import common.db.fields


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('acls', '0014_loginassetacl_rules'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConnectMethodACL',
            fields=[
                ('created_by', models.CharField(blank=True, max_length=128, null=True, verbose_name='Created by')),
                ('updated_by', models.CharField(blank=True, max_length=128, null=True, verbose_name='Updated by')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Date created')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='Date updated')),
                ('comment', models.TextField(blank=True, default='', verbose_name='Comment')),
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=128, unique=True, verbose_name='Name')),
                ('priority', models.IntegerField(default=50, help_text='1-100, the lower the value will be match first',
                                                 validators=[django.core.validators.MinValueValidator(1),
                                                             django.core.validators.MaxValueValidator(100)],
                                                 verbose_name='Priority')),
                ('action', models.CharField(default='reject', max_length=64, verbose_name='Action')),
                ('is_active', models.BooleanField(default=True, verbose_name='Active')),
                ('users', common.db.fields.JSONManyToManyField(default=dict, to='users.User', verbose_name='Users')),
                ('connect_methods', models.JSONField(default=list, verbose_name='Connect methods')),
                (
                    'reviewers',
                    models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL, verbose_name='Reviewers')),
            ],
            options={
                'ordering': ('priority', '-is_active', 'name'),
                'abstract': False,
            },
        ),
    ]
