from django.db import models
from tinymce.models import HTMLField


class GoodsManager(models.Manager):
    def create(self, gtitle, price, unit, ginfo, gdetail, gstore, gcomment, gclick, gtype, gpic, gthumb):
        goods = Goods()
        goods.gtitle = gtitle
        goods.price = price
        goods.unit = unit
        goods.ginfo = ginfo
        goods.gdetail = gdetail
        goods.gsotre = gstore
        goods.gcomment = gcomment
        goods.gclick = gclick
        goods.gtype_id = gtype
        goods.gthumb = gthumb
        goods.save()


class TypeInfo(models.Model):
    goods_type = models.CharField(max_length=20)
    isDelete = models.BooleanField(default=False)

    #解决插入货物信息时，选择外键不显示中文的问题,对象调用str方法
    def __str__(self):
        return self.goods_type


class Goods(models.Model):
    gtitle = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    unit = models.CharField(max_length=10)
    ginfo = models.TextField()
    gdetail = models.TextField(blank=True)
    gsotre = models.IntegerField(blank=True)
    gcomment = HTMLField(blank=True)
    gclick = models.IntegerField()
    gtype = models.ForeignKey(TypeInfo)
    isDelete = models.BooleanField(default=False)
    gthumb = models.ImageField(upload_to='df_goods/goods')
    gpic = models.ImageField(upload_to='df_goods/pic_detail')
    gmanager = GoodsManager()

    def __str__(self):
        return self.gtitle
