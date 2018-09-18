# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('df_user', '0006_cart'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('user', models.CharField(max_length=18, unique=True, db_index=True)),
                ('password', models.CharField(max_length=40)),
                ('mail', models.CharField(max_length=16)),
                ('order_num', models.IntegerField(default=0)),
            ],
        ),
        migrations.AlterField(
            model_name='cart',
            name='user',
            field=models.ForeignKey(to='df_user.UserInfo'),
        ),
        migrations.AlterField(
            model_name='useraddress',
            name='user',
            field=models.ForeignKey(to='df_user.UserInfo'),
        ),
        migrations.DeleteModel(
            name='UserRegister',
        ),
    ]
