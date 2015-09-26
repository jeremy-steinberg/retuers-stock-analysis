from lxml import html
import requests


NZX50_URL = 'http://topforeignstocks.com/indices/components-of-the-nzsx-50-index/'

# the entire stock list path is: '//*[@id="yfncsumtab"]/tbody/tr[2]/td[1]/table[2]/tbody/tr/td/table/tbody/tr[i]/td[1]/b/a/text()' #
# i is in the range 2 to 51 (including 51) for the 50 stocks

STOCK_XPATH_P1 = '//*[@id="tablepress-915"]/tbody/tr['
STOCK_XPATH_P2 = ']/td[3]/text()'


STOCK_LIST_XML = []
STOCK_LIST_TICKERS = []

# the tr goes from [2] to [51]

for i in range(1, 50):
     complete_path = STOCK_XPATH_P1 + str(i) + STOCK_XPATH_P2
     STOCK_LIST_XML.append(complete_path)



#=================FUNCTIONS=================#

def get_NZX50_xml():
    global NZX50_xml

    url = NZX50_URL
    page = requests.get(url)
    NZX50_xml = html.fromstring(page.text)
    return NZX50_xml

def get_NZX50_tickers(xpath):
    global NZX50_xml

    return NZX50_xml.xpath(xpath)



get_NZX50_xml()



for item in STOCK_LIST_XML:
    STOCK_LIST_TICKERS.append(get_NZX50_tickers(item))

print (STOCK_LIST_TICKERS)

# print (test())

# //*[@id="tablepress-915"]/tbody/tr[1]/td[3]
# //*[@id="tablepress-915"]/tbody/tr[2]/td[3]
# //*[@id="tablepress-915"]/tbody/tr[4]/td[3]
# //*[@id="tablepress-915"]/tbody/tr[50]/td[3]



