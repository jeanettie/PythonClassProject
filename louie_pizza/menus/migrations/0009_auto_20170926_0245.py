# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-26 02:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menus', '0008_auto_20170915_0413'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='category',
            new_name='name',
        ),
    ]