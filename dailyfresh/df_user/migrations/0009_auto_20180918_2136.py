# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('df_user', '0008_auto_20180918_2131'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='user_name',
            new_name='user',
        ),
    ]
