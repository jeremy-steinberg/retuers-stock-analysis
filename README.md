# retuers-stock-analysis


Takes a stock list in a text file, scrapes stock analyses from reuters, and inserts into an excel spreadsheet


The text file has to be called stocks.txt
Each stock should be entered manually into the file, separated by a comma (e.g. GOOG,APPL,NFLX)
do not put a space after each comma

required libraries: requests, lxml, openpyxl

install using command prompt or powershell using the following:

pip install requests
pip install lxml
pip install openpyxl