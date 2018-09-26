# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('df_user', '0001_initial'),
        ('df_goods', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('subtotal', models.DecimalField(max_digits=6, decimal_places=2)),
                ('amount', models.IntegerField()),
                ('goods', models.ForeignKey(to='df_goods.Goods')),
            ],
        ),
        migrations.CreateModel(
            name='OrderInfo',
            fields=[
                ('oid', models.CharField(primary_key=True, max_length=50, serialize=False)),
                ('odatetime', models.DateTimeField(auto_now=True)),
                ('opay', models.BooleanField(default=False)),
                ('ototal', models.IntegerField()),
                ('oaddress', models.CharField(max_length=150)),
                ('user', models.ForeignKey(to='df_user.UserInfo')),
            ],
        ),
        migrations.AddField(
            model_name='orderdetail',
            name='order',
            field=models.ForeignKey(to='df_order.OrderInfo'),
        ),
    ]
