from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from . import  models
import hashlib


def register(request):
    return render(request, 'df_user/register.html')


def registerHandle(request):
    #插入数据库
    user_register = models.UserRegister()
    user_register.user = request.POST['user_name']
    user_register.mail = request.POST['email']
    #判断两次输入的密码是否一致
    pwd2 = request.POST['cpwd']
    pwd1 = request.POST['pwd']
    if pwd1 == pwd2:
        #密码加密
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
    result = models.UserRegister.objects.filter(user=user)
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


def user_center(request):
    # 如果session存在，表示登入过则获取页面
    if 'user_id' in request.session.keys():
        result = models.UserRegister.objects.get(user=request.session['user_name'])
        user = result.user
        mail = result.mail
        return render(request, 'df_user/user_center_info.html', {'user': user, 'mail': mail})
    # 如果cookie不存在，则要重新登入(转入到登陆界面)
    return redirect('/user/login')


def user_center_order(request):
    if 'user_id' in request.session.keys():
        return render(request, 'df_user/user_center_order.html')
    return redirect('/user/login')


def user_center_site(request):
    if 'user_id' in request.session.keys():
        id = request.session['user_id']
        info = models.UserAddress.objects.filter(user_id=id)[0]
        context = {
            'recipients': info.recipients,
            'detail_address': info.detail_address,
            'zip_code': info.zip_code,
            'mobile_phone': info.mobile_phone
        }
        return render(request, 'df_user/user_center_site.html', context)
    return redirect('/user/login')


def user_site_handle(request):
    post = request.POST
    user_site = models.UserAddress()
    user_site.recipients = post['recipients']
    user_site.detail_address = post['detail_address']
    user_site.zip_code = post['zip_code']
    user_site.mobile_phone = post['mobile_phone']
    user_site.user_id = request.session['user_id']
    user_site.save()
    return redirect('/user/user_center_site')















