from django.db import models
from df_goods.models import *


class UserInfo(models.Model):
    user = models.CharField(max_length=18, unique=True, db_index=True)
    password = models.CharField(max_length=40)
    mail = models.CharField(max_length=16)
    order_num = models.IntegerField(default=0)

    def __str__(self):
        return self.user


class UserAddress(models.Model):
    recipients = models.CharField(max_length=16)
    detail_address = models.CharField(max_length=40)
    mobile_phone = models.CharField(max_length=11)
    zip_code = models.IntegerField()
    user = models.ForeignKey(UserInfo)


class Cart(models.Model):
    user = models.ForeignKey(UserInfo)
    goods = models.ForeignKey(Goods)
    amount = models.IntegerField()





