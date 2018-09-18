# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('df_goods', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods',
            name='gthumb',
            field=models.ImageField(default=1, upload_to='df_goods/goods'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='goods',
            name='gpic',
            field=models.ImageField(upload_to='df_goods/pic_detail'),
        ),
    ]
