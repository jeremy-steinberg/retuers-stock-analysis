from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^add_stock$', views.add_stock, name='add_stock'),
    url(r'^remove_stock$', views.remove_stock, name='remove_stock'),
    url(r'^stocks$', views.stocks, name='stocks'),
]