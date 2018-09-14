# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('df_user', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userregister',
            old_name='passwork',
            new_name='password',
        ),
    ]
