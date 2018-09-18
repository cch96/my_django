# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('df_goods', '0002_auto_20180915_2124'),
        ('df_user', '0005_useraddress_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('goods', models.ForeignKey(to='df_goods.Goods')),
                ('user', models.ForeignKey(to='df_user.UserRegister')),
            ],
        ),
    ]
