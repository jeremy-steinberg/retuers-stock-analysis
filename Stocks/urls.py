from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^add_stock/(?P<code>.+)$', views.add_stock, name='add_stock'),
    url(r'^update_stocks$', views.update_stocks, name='update_stocks'),
    url(r'^stocks$', views.stocks, name='stocks'),
]