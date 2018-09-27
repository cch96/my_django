from django.db import models
from df_user.models import *


class OrderInfo(models.Model):
    oid = models.CharField(max_length=50, primary_key=True)
    user = models.ForeignKey('df_user.UserInfo')
    # auto_now 会把时间设置为当前时间
    odatetime = models.DateTimeField(auto_now=True)
    opay = models.BooleanField(default=False)
    ototal = models.IntegerField()
    oaddress = models.ForeignKey(UserAddress)


class OrderDetail(models.Model):
    goods = models.ForeignKey('df_goods.Goods')
    subtotal = models.DecimalField(max_digits=6, decimal_places=2)
    amount = models.IntegerField()
    order = models.ForeignKey('OrderInfo')

