# Generated by Django 2.1.7 on 2019-05-21 08:19

import common.utils.django
from django.conf import settings
from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0019_auto_20190304_1459'),
        ('applications', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('perms', '0004_assetpermission_actions'),
    ]

    operations = [
        migrations.CreateModel(
            name='RemoteAppPermission',
            fields=[
                ('org_id', models.CharField(blank=True, db_index=True, default='', max_length=36, verbose_name='Organization')),
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=128, verbose_name='Name')),
                ('is_active', models.BooleanField(default=True, verbose_name='Active')),
                ('date_start', models.DateTimeField(db_index=True, default=django.utils.timezone.now, verbose_name='Date start')),
                ('date_expired', models.DateTimeField(db_index=True, default=common.utils.django.date_expired_default, verbose_name='Date expired')),
                ('created_by', models.CharField(blank=True, max_length=128, verbose_name='Created by')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Date created')),
                ('comment', models.TextField(blank=True, verbose_name='Comment')),
                ('remote_apps', models.ManyToManyField(blank=True, related_name='granted_by_permissions', to='applications.RemoteApp', verbose_name='RemoteApp')),
                ('user_groups', models.ManyToManyField(blank=True, to='users.UserGroup', verbose_name='User group')),
                ('users', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'RemoteApp permission',
                'ordering': ('name',),
            },
        ),
        migrations.AlterField(
            model_name='assetpermission',
            name='user_groups',
            field=models.ManyToManyField(blank=True, to='users.UserGroup', verbose_name='User group'),
        ),
        migrations.AlterField(
            model_name='assetpermission',
            name='users',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
        migrations.AlterUniqueTogether(
            name='remoteapppermission',
            unique_together={('org_id', 'name')},
        ),
    ]
