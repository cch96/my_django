from django.conf.urls import url
from . import views


urlpatterns = [
   url(r'^$', views.index),
   url(r'^index/', views.index),
   url(r'^gdetail(\d+)', views.goods_detail),
   url(r'^list(\d+)_(\d+)_(\d+)', views.goods_list),
]