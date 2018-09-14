# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('df_user', '0004_useraddress'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraddress',
            name='user',
            field=models.ForeignKey(default=1, to='df_user.UserRegister'),
            preserve_default=False,
        ),
    ]
