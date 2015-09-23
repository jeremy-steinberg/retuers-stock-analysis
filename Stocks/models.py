from django.db import models
from django.utils import timezone


class Stock(models.Model):
    code = models.CharField(max_length=200)
    
    def __str__(self):
        return self.code
    
    @staticmethod
    def crete_stock(code):
        stock = Stock(code=code)
        stock.save()
        return stock
    
class StockValue(models.Model):
    stock_id = models.CharField(max_length=200)
    buy = models.IntegerField()
    outperform = models.IntegerField()
    hold = models.IntegerField()
    underperform = models.IntegerField()
    sell = models.IntegerField()
    no_opinion = models.IntegerField()
    mean = models.FloatField()
    consensus = models.CharField(max_length=200)
    dividend = models.CharField(max_length=200)
    price_earnings = models.CharField(max_length=200)
    mean_last_month=models.FloatField()
    time = models.TimeField()
    
    def __str__(self):
        return self.id
    
    @staticmethod
    def create_stock_value(stock_id, buy, outperform, hold, underperform, sell,
                           no_opinion, mean, consensus, dividend, price_earnings,
                           mean_last_month):
        stock_value = StockValue(stock_id=stock_id, buy= buy, outperform= outperform,
                                 hold= hold, underperform=underperform, sell= sell,
                                 no_opinion= no_opinion,mean= mean, 
                                 consensus=consensus, dividend=dividend, price_earnings=price_earnings,
                                 mean_last_month=mean_last_month, time= timezone.now())
        stock_value.save()
        return stock_value
    
    def get_stock_code(self):
        stock = Stock.objects.get(pk=self.stock_id)
        return stock.code
    
    def get_mean_difference(self):
        difference = self.mean - self.mean_last_month
        if difference == 0:
            difference = ""
        return difference