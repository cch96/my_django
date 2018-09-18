from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from df_user.models import *
from df_goods.models import *
import hashlib


def check_login(func):
    # 如果session不存在，则要重新登入(转入到登陆界面)
    def wrapper(request):
        if 'user_id' not in request.session.keys():
            return redirect('/user/login')
        return func(request)
    return wrapper


def check_login1(request):
    if 'user_id' in request.session.keys():
        return JsonResponse({'code':1, 'msg':{'user_name': request.session['user_name']}})
    else:
        return JsonResponse({'code':0, 'msg':{}})


def register(request):
    return render(request, 'df_user/register.html')


def registerHandle(request):
    # 插入数据库
    user_register = models.UserInfo()
    user_register.user = request.POST['user_name']
    user_register.mail = request.POST['email']
    # 判断两次输入的密码是否一致
    pwd2 = request.POST['cpwd']
    pwd1 = request.POST['pwd']
    if pwd1 == pwd2:
        # 密码加密
        s1 = hashlib.sha1()
        s1.update(pwd1.encode('utf8'))
        user_register.password = s1.hexdigest()
        user_register.save()
        return render(request, 'df_user/login.html')


def login(request):
    user_name = ''
    if 'user' in request.COOKIES:
        user_name = request.COOKIES['user'].encode('latin-1').decode('utf-8')
    return render(request, 'df_user/login.html', {'user_name': user_name})


def login_handle(request):
    user = request.POST['username']
    password = request.POST['pwd']
    remember = request.POST.get('remember_user', 0)
    # 在数据库中查找登陆页面提交的用户名
    result = UserInfo.objects.filter(user=user)
    # 如果用户名不存在
    if not result:
        return render(request, 'df_user/login.html', {'error_user': True, 'user_name': user})

    # 用户名存在,看密码是否正确
    s1 = hashlib.sha1()
    s1.update(password.encode('utf8'))
    # 密码错误重新回到登入界面
    if s1.hexdigest() != result[0].password:
        return render(request, 'df_user/login.html', {'error_pwd': True, 'user_name': user})

    # 如果正确则进入用户界面,并设置cookie,并且转向
    response = HttpResponseRedirect('/user/user_center_info')
    if remember:
        response.set_cookie('user', user.encode('utf-8').decode('latin-1'))
    else:
        # 不记住就cookie就失效
        response.set_cookie('user', '', max_age=-1)
    # 设置session在保证用户信息安全的情况下，记录用户行为
    #TODO 这里最好加一个redis把用户的数据先缓存到reids
    request.session['user_id'] = result[0].id
    request.session['user_name'] = result[0].user
    request.session.set_expiry(0)
    return response


@check_login
def user_center(request):
    # 获取页面
    result = UserInfo.objects.get(user=request.session['user_name'])
    user = result.user
    mail = result.mail
    looks = request.COOKIES['looks'].split(',')
    looks = Goods.gmanager.filter(pk__in=looks)
    return render(request, 'df_user/user_center_info.html', {'user': user, 'mail': mail, 'looks': looks})


@check_login
def user_center_order(request):
    return render(request, 'df_user/user_center_order.html')


@check_login
def user_center_site(request):
    id = request.session['user_id']
    info = UserAddress.objects.filter(user_id=id)
    if info:
        context = {
            'recipients': info.recipients,
            'detail_address': info.detail_address,
            'zip_code': info.zip_code,
            'mobile_phone': info.mobile_phone
        }
    else:
        context = {
            'recipients': '',
            'detail_address': '',
            'zip_code': '',
            'mobile_phone': ''
        }

    return render(request, 'df_user/user_center_site.html', context)


def user_site_handle(request):
    post = request.POST
    user_site = UserAddress()
    user_site.recipients = post['recipients']
    user_site.detail_address = post['detail_address']
    user_site.zip_code = post['zip_code']
    user_site.mobile_phone = post['mobile_phone']
    user_site.user_id = request.session['user_id']
    user_site.save()
    return redirect('/user/user_center_site')


def cart(request):
    list = Cart.objects.filter(user_id=request.session['user_id'])
    cart_list = []
    for item in list:
        cart_list.append(item.goods)
    return render(request, 'df_user/cart.html', {'list': cart_list})


def add_cart(request):
    # 如果是ajax请求
    if request.is_ajax():
        # 购物车数据库增加数据
        cart = Cart()
        cart.goods_id = request.GET['goods']
        cart.user_id = request.session['user_id']
        cart.save()
        # 修改用户的购物车里的商品数量
        user = UserInfo.objects.get(pk=request.session['user_id'])
        user.order_num = user.order_num + 1
        user.save()
        return JsonResponse({'status': 'ok', 'order_num': user.order_num})
    # 否则


def quit(request):
    request.session.flush()
    return HttpResponseRedirect('/')

