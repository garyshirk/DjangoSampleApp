# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-21 15:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_item_backorder'),
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=20)),
                ('lastname', models.CharField(max_length=20)),
                ('division', models.CharField(max_length=200)),
                ('timeonjob', models.IntegerField(default=0)),
            ],
        ),
    ]
