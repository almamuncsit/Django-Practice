# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-19 20:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Title')),
                ('embed_code', models.TextField(verbose_name='Embed Code')),
            ],
        ),
    ]
