# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserRegister',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('user', models.CharField(max_length=16, unique=True, db_index=True)),
                ('passwork', models.CharField(max_length=16)),
                ('mail', models.CharField(max_length=16)),
            ],
        ),
    ]
