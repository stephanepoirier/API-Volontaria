# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-16 15:40
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('volunteer', '0007_auto_20180316_1417'),
    ]

    operations = [
        migrations.AddField(
            model_name='cell',
            name='managers',
            field=models.ManyToManyField(blank=True, related_name='managed_cell', to=settings.AUTH_USER_MODEL, verbose_name='Managers'),
        ),
    ]
