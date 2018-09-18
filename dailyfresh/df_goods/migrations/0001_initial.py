# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('gtitle', models.CharField(max_length=20)),
                ('price', models.DecimalField(max_digits=5, decimal_places=2)),
                ('unit', models.CharField(max_length=10)),
                ('ginfo', models.TextField()),
                ('gdetail', models.TextField(blank=True)),
                ('gsotre', models.IntegerField(blank=True)),
                ('gcomment', tinymce.models.HTMLField(blank=True)),
                ('gclick', models.IntegerField()),
                ('isDelete', models.BooleanField(default=False)),
                ('gpic', models.ImageField(upload_to='df_goods')),
            ],
        ),
        migrations.CreateModel(
            name='TypeInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('goods_type', models.CharField(max_length=20)),
                ('isDelete', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='goods',
            name='gtype',
            field=models.ForeignKey(to='df_goods.TypeInfo'),
        ),
    ]
