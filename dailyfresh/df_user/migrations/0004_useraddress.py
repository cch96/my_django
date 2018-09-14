# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('df_user', '0003_auto_20180913_1529'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAddress',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('recipients', models.CharField(max_length=16)),
                ('detail_address', models.CharField(max_length=40)),
                ('mobile_phone', models.IntegerField()),
                ('zip_code', models.IntegerField()),
            ],
        ),
    ]
