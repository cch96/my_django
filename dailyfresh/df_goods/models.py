from django.db import models


class TypeInfo(models.Model):
    goods_type = models.CharField(max_length=20)


class Goods(models.Model):
    title = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    unit = models.CharField(max_length=10)
    goods_info = models.TextField()
    goods_detail = models.TextField()
    goods_sotre = models.IntegerField()
    goods_comment = models.HTMLF
    # TODO  昨天从这里结束准备安装富文本编辑器
