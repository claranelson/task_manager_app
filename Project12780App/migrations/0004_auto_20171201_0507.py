# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-01 05:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Project12780App', '0003_auto_20171125_2140'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(max_length=40)),
                ('Password', models.CharField(max_length=40)),
            ],
        ),
        migrations.AddField(
            model_name='task',
            name='User',
            field=models.CharField(default='trial', max_length=40),
            preserve_default=False,
        ),
    ]
