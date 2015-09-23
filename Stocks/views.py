from django.shortcuts import render
from django.http import HttpResponseRedirect
from Stocks import models

def add_stock(request, code):
    try:
        models.Stock.objects.get(code=code)
    except models.Stock.DoesNotExist:
        models.Stock.crete_stock(code)
    return HttpResponseRedirect("/stocks/stocks")

def stocks(request):
    models.StockValue.update_stock_values()
    stocks = models.Stock.objects.all()
    stock_values = []
    for stock in stocks:
        stock_value = models.StockValue.objects.filter(stock_id=stock.pk).order_by("time").last()
        if stock_value != None:
            stock_values.append(stock_value)
    context = {'stock_values': stock_values}
    return render(request, 'stocks.html', context)