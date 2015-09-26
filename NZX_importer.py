from lxml import html
import requests


NZX50_URL = 'http://topforeignstocks.com/indices/components-of-the-nzsx-50-index/'
NZX_URL = 'https://www.nzx.com/markets/NZSX/securities'

STOCK_XPATH_50 = '//*[@id="tablepress-915"]/tbody/tr/td[3]/text()'
STOCK_XPATH = '//*[@id="instruments"]/table/tbody/tr/td[1]/a/text()'

STOCK_LIST_50_TICKERS = []
STOCK_LIST_TICKERS = []


#=================FUNCTIONS=================#

## these functions get the stock ticker names from the two urls
## the get_NZX50 functions get the top 50 stocks
## the get_NZX function get the entire stock exchange stocks (170 at time of writing)

def get_NZX50_xml():
    global NZX50_xml

    url = NZX50_URL
    page = requests.get(url)
    NZX50_xml = html.fromstring(page.text)
    return NZX50_xml

def get_NZX50_tickers(xpath):

    return NZX50_xml.xpath(xpath)

def get_NZX_xml():
    global NZX_xml

    url = NZX_URL
    page = requests.get(url)
    NZX_xml = html.fromstring(page.text)
    return NZX_xml

def get_NZX_tickers(xpath):

    return NZX_xml.xpath(xpath)



#=================EXECUTE FUNCTIONS=================#

get_NZX50_xml()
get_NZX_xml()



STOCK_LIST_TICKERS = get_NZX_tickers(STOCK_XPATH)
print (STOCK_LIST_TICKERS)

STOCK_LIST_50_TICKERS = get_NZX50_tickers(STOCK_XPATH_50)
print (STOCK_LIST_50_TICKERS)





