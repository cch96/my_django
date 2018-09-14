from django.contrib import admin
from .models import *

'''
class InlineUserAddress(admin.StackedInline):
    model = UserAddress
    extra = 3
'''
# TODO 有收货数据后把内联给做完
class MyAdmin(admin.ModelAdmin):
    list_display = ['user', 'mail']
    #inlines = [InlineUserAddress]

admin.site.register(UserAddress)
admin.site.register(UserRegister, MyAdmin)
