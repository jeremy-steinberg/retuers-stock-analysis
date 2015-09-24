from django.conf.urls import include, url
from django.http import HttpResponse

def home(request):
    return HttpResponse("<b>The thing!!!!!!</b>")

urlpatterns = [
    url(r'^$',home),
    url(r'^stocks/', include('Stocks.urls')),
]