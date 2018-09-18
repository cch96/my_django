from django.contrib import admin
from .models import *

'''
class InlineUserAddress(admin.StackedInline):
    model = UserAddress
    extra = 3
'''
# TODO 有收货数据后把内联给做完
class MyUser(admin.ModelAdmin):
    list_display = ['user', 'mail']
    # inlines = [InlineUserAddress]


class MyCart(admin.ModelAdmin):
    list_display = ['user', 'goods']

admin.site.register(UserAddress)
admin.site.register(UserInfo, MyUser)
admin.site.register(Cart, MyCart)
