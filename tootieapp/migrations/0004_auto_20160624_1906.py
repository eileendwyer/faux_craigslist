# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-24 19:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tootieapp', '0003_posting_village'),
    ]

    operations = [
        migrations.RenameField(
            model_name='posting',
            old_name='name',
            new_name='category',
        ),
    ]