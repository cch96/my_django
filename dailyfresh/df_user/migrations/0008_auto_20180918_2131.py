# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('df_user', '0007_auto_20180918_1905'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='user',
            new_name='user_name',
        ),
    ]
