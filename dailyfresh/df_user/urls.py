from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^register$', views.register),
    url(r'^registerHandle$', views.registerHandle),
    url(r'^login$', views.login),
    url('^login_handle$', views.login_handle),
    url(r'^user_center_info', views.user_center),
    url(r'^user_center_order', views.user_center_order),
    url(r'^user_center_site', views.user_center_site),
    url(r'^user_site_handle', views.user_site_handle)
]