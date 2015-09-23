from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^add_stock/(?P<code>.+)$', views.add_stock, name='add_stock'),
    url(r'^stocks$', views.stocks, name='stocks'),
]