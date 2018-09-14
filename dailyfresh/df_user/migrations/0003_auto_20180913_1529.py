# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('df_user', '0002_auto_20180913_1515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userregister',
            name='password',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='userregister',
            name='user',
            field=models.CharField(max_length=18, unique=True, db_index=True),
        ),
    ]
