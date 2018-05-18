# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-05-18 15:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0002_user_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=255)),
                ('seller', models.CharField(max_length=255)),
                ('date_posted', models.CharField(max_length=255)),
                ('ammount', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_of_products', to='first_app.User')),
            ],
        ),
    ]