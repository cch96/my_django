from django.db import models


class UserRegister(models.Model):
    user = models.CharField(max_length=18, unique=True, db_index=True)
    password = models.CharField(max_length=40)
    mail = models.CharField(max_length=16)


class UserAddress(models.Model):
    recipients = models.CharField(max_length=16)
    detail_address = models.CharField(max_length=40)
    mobile_phone = models.IntegerField()
    zip_code = models.IntegerField()
    user = models.ForeignKey(UserRegister)





