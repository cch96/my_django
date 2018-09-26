import time
import json

from django.shortcuts import render
from django.http import JsonResponse
from django.db import transaction
from df_order.models import *
from df_user.models import *


def place_order(request):
    order_id = request.GET['order_id']
    order_info = OrderInfo.objects.get(oid=order_id)
    user_address = order_info.oaddress
    order_detail = order_info.orderdetail_set.all()
    context = {
        'order_info': order_info,
        'order_detail': order_detail,
        'user_address': user_address
    }
    return render(request, 'df_order/place_order.html', context)


def to_order(request):
    # 保存到订单表，删除购物车表数据，保证原子性

    tran_id = transaction.savepoint()
    if request.method == 'GET':
        goods_id = request.GET['goods_id']
        amount = request.GET['amount']
        subtotal = request.GET['subtotal']
        # 订单信息
        order_info = OrderInfo()
        order_info.oid = str(int(time.time()))
        order_info.user_id = request.session['user_id']
        order_info.opay = False
        order_info.ototal = float(subtotal)
        order_info.oaddress = UserAddress.objects.filter(user_id=order_info.user_id)[0]
        order_info.save()
        # 商品详情
        order_detail = OrderDetail()
        order_detail.goods_id = goods_id
        order_detail.subtotal = float(subtotal)
        order_detail.amount = int(amount)
        order_detail.order = order_info
        order_detail.save()
    try:
        if request.method == 'POST':
            # 存下选中的购物车的商品信息到订单
            goods_list = request.POST['goods_list']
            goods_list = json.loads(goods_list)
            # 订单信息
            total = request.POST['total']
            order_info = OrderInfo()
            order_info.oid = str(int(time.time()))
            order_info.user_id = request.session['user_id']
            order_info.opay = False
            order_info.ototal = total
            order_info.oaddress = UserAddress.objects.filter(user_id=order_info.user_id)[0]
            order_info.save()
            # 订单细节
            for goods in goods_list:
                order_detail = OrderDetail()
                order_detail.goods_id = goods['goods_id']
                order_detail.subtotal = goods['subtotal']
                order_detail.amount = goods['amount']
                order_detail.order = order_info
                order_detail.save()

            # 删除购物车表中的信息
            for goods in goods_list:
                cart_id = goods['cart_id']
                goods = Cart.objects.get(id=cart_id)
                goods.delete()
            # 删除用户购物车商品个数
            user_info = UserInfo.objects.get(pk=request.session['user_id'])
            user_info.order_num = user_info.order_num - len(goods_list)
            user_info.save()

    except Exception as e:
        print(e)
        transaction.savepoint_rollback(tran_id)
        return JsonResponse({'code': '0', 'msg': ''})

    return JsonResponse({'code': '1', 'msg': order_info.oid})
