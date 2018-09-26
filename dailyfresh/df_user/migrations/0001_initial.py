# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('df_goods', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('amount', models.IntegerField()),
                ('goods', models.ForeignKey(to='df_goods.Goods')),
            ],
        ),
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
        migrations.AddField(
            model_name='useraddress',
            name='user',
            field=models.ForeignKey(to='df_user.UserInfo'),
        ),
        migrations.AddField(
            model_name='cart',
            name='user',
            field=models.ForeignKey(to='df_user.UserInfo'),
        ),
    ]
