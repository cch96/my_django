from django.shortcuts import render
from . import models
from django.core import paginator


def index(request):
    types = models.TypeInfo.objects.filter(isDelete=False)
    list = []
    for type in types:
        list.append({'type': type,
                     'data': type.goods_set.all().order_by('gclick')[0:4]})
    return render(request, 'df_goods/index.html', {'list': list})


def goods_detail(request, no):
    goods = models.Goods.gmanager.get(pk=no)
    list = models.Goods.gmanager.filter(gtype_id=goods.gtype_id).order_by('gclick')
    response = render(request, 'df_goods/detail.html', {'goods': goods, 'list': list[: 2]})
    # 第一此添加推荐商品
    if 'looks' not in request.COOKIES.keys():
        looks = no
    else:
        list = request.COOKIES['looks'].split(',')
        list.append(no)
        if len(list) > 5:
            list.pop(1)
        looks = ','.join(list)
    response.set_cookie('looks', looks)
    return response


def goods_list(request, type, page, sorted):
    # type为0时取出所有商品
    if type == '0':
        goods_list = models.Goods.gmanager.all()
        type_name = None
    else:
        # 取出对应类的所有商品
        type_name = models.TypeInfo.objects.get(pk=type).goods_type
        goods_list = models.Goods.gmanager.filter(gtype_id=type)
        result = ''

    # 对取出的商品进行排序
    if sorted == '1':
        # 排序为1就是按时间排序
        result = goods_list.order_by('id')
    if sorted == '2':
        # 排序为2就是按点击率排名
        result = goods_list.order_by('price')
    if sorted == '3':
        # 排序为3就是按点击率排名
        result = goods_list.order_by('gclick')

    # 推荐商品
    adv_list = result[: 2]
    # 将结果进行分页
    pages = paginator.Paginator(result, 14)
    goods_list = pages.page(page)
    context = {
                'type': type_name,
                'goods_list': goods_list,
                'adv_list': adv_list,
                'sorted': sorted,
                'type_id': type
               }
    return render(request, 'df_goods/list.html', context)

