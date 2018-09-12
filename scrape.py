from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv
from datetime import datetime
import sqlite3

#conn = sqlite3.connect('options.db')

#c = conn.cursor()

#c.execute('')

# variable for url
quote_page = 'https://finance.yahoo.com/quote/MSFT/options?date=1545350400'

# query the website and return the html to the variable page
page = urlopen(quote_page)

# now we parse with beautifulsoup
soup = BeautifulSoup(page, 'html.parser')

#dateList = []
#strikeList = []
#date_box = soup.find_all('td', attrs={'class': 'data-col1'})
# date = date_box.text.strip()
#for item in date_box:
#    date = item.text.strip()
#    dateList.append(date)

#strike_box = soup.find_all('td', attrs={'class': 'data-col2'})

#for item in strike_box:
#    strike = item.text.strip()
#    strikeList.append(strike)

parentlist = []
onerow = []

row_box = soup.find('tr', attrs={'class': 'data-row5'})
for col in row_box.find_all('td'):
    coltext = col.get_text()
    onerow.append(coltext)
parentlist.append(onerow)

onerow = []
row_box = soup.find('tr', attrs={'class': 'data-row6'})
for col in row_box.find_all('td'):
    coltext = col.get_text()
    onerow.append(coltext)
parentlist.append(onerow)

onerow = []
row_box = soup.find('tr', attrs={'class': 'data-row7'})
for col in row_box.find_all('td'):
    coltext = col.get_text()
    onerow.append(coltext)
parentlist.append(onerow)

onerow = []
row_box = soup.find('tr', attrs={'class': 'data-row8'})
for col in row_box.find_all('td'):
    coltext = col.get_text()
    onerow.append(coltext)
parentlist.append(onerow)

onerow = []
row_box = soup.find('tr', attrs={'class': 'data-row9'})
for col in row_box.find_all('td'):
    coltext = col.get_text()
    onerow.append(coltext)
parentlist.append(onerow)

onerow = []
row_box = soup.find('tr', attrs={'class': 'data-row10'})
for col in row_box.find_all('td'):
    coltext = col.get_text()
    onerow.append(coltext)
parentlist.append(onerow)

with open('index.csv', 'a') as csv_file:
    writer = csv.writer(csv_file)
    for row in parentlist:
        writer.writerow(row)