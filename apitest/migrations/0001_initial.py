# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-07 00:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(blank=True, default='', max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('age', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('sex', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
    ]
