from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^place_order$', views.place_order),
    url(r'^to_order', views.to_order),
    url(r'^place_order', views.place_order)
]