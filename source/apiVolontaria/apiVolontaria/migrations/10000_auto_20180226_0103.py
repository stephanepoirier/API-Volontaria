# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-26 01:03
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('apiVolontaria', '9999_user_email_unique'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActionToken',
            fields=[
                ('key', models.CharField(max_length=40, primary_key=True, serialize=False, verbose_name='Key')),
                ('type', models.CharField(choices=[('account_activation', 'Account activation'), ('password_change', 'Password change')], max_length=100, verbose_name='Type of action')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Creation date')),
                ('expires', models.DateTimeField(blank=True, verbose_name='Expiration date')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='activation_token', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
        migrations.RemoveField(
            model_name='activationtoken',
            name='user',
        ),
        migrations.DeleteModel(
            name='ActivationToken',
        ),
    ]
