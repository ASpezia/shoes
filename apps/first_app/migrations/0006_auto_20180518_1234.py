# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-05-18 17:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0005_auto_20180518_1217'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='user_buyong',
            new_name='user_buying',
        ),
        migrations.AlterField(
            model_name='item',
            name='date_posted',
            field=models.DateField(max_length=255),
        ),
    ]
