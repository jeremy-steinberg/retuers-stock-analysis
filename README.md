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

# retuers-stock-analysis website

Install Django https://docs.djangoproject.com/en/1.8/topics/install/#install-the-django-code

create a DB:
python manage.py migrate

run the website
python manage.py runserver

open http://127.0.0.1:8000/stocks/stocks