from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from Stocks import models

from Stocks.reuters_library import ReutersLibrary

def update_stocks(request):
    stocks = models.Stock.objects.all()
    for stock in stocks:
        values = ReutersLibrary.get_stock_values(stock.code)
        if len(values) > 7:
            models.StockValue.create_stock_value(stock.pk, values[0], values[1],
                                                 values[2], values[3], values[4],
                                                  values[5], values[6],values[7],
                                                  values[8], values[9], values[10])
            
    return HttpResponseRedirect("/stocks/stocks")


def add_stock(request, code):
    try:
        models.Stock.objects.get(code=code)
    except models.Stock.DoesNotExist:
        models.Stock.crete_stock(code)
    return HttpResponseRedirect("/stocks/stocks")

def stocks(request):
    stocks = models.Stock.objects.all()
    stock_values = []
    for stock in stocks:
        stock_value = models.StockValue.objects.filter(stock_id=stock.pk).order_by("time").last()
        if stock_value != None:
            stock_values.append(stock_value)
    context = {'stock_values': stock_values}
    return render(request, 'stocks.html', context)