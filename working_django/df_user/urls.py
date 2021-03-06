from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^register$', views.register),
    url(r'^registerHandle$', views.registerHandle),
    url(r'^login$', views.login),
    url('^login_handle$', views.login_handle),
    url(r'^user_center_info', views.user_center),
    url(r'^user_center_site', views.user_center_site),
    url(r'^user_site_handle', views.user_site_handle),
    url(r'^check_login1', views.check_login1),
    url(r'^quit', views.quit),
    url(r'^cart', views.cart),
    url(r'^add_cart', views.add_cart),
    url(r'^delete_cart', views.delete_cart),
    url(r'^user_center_order/(\d*)', views.user_center_order)
]