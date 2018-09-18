# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('df_user', '0010_auto_20180918_2138'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userinfo',
            old_name='user_name',
            new_name='user',
        ),
    ]
