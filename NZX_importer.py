from lxml import html
import requests


## note this is written for python 3, unlike previous programs in project

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


def generate_NZX50_list():
    get_NZX50_xml()
    STOCK_LIST_50_TICKERS = get_NZX50_tickers(STOCK_XPATH_50)
    return STOCK_LIST_50_TICKERS

def generate_NZX_list():
    get_NZX_xml()
    STOCK_LIST_TICKERS = get_NZX_tickers(STOCK_XPATH)
    for i in range (len(STOCK_LIST_TICKERS)):
        STOCK_LIST_TICKERS[i] += ".NZ"
    return STOCK_LIST_TICKERS

#=================EXECUTE FUNCTIONS=================#







print (generate_NZX_list())
print (generate_NZX50_list())





