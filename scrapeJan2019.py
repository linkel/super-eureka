# This version of scrape scrapes the Jan 2019 calls. The other file grabs the Dec 2018 ones.
# Just a hacky copy for now since getting the data is more important to me than prettying the code
# TODO: Figure out how to automate the date stuff

from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv
from datetime import datetime
import sqlite3

conn = sqlite3.connect('options.db')

c = conn.cursor()

# variable for url
quote_page = 'https://finance.yahoo.com/quote/MSFT/options?date=1547769600'
apple_page = 'https://finance.yahoo.com/quote/AAPL/options?date=1547769600'

# query the website and return the html to the variable page
page = urlopen(quote_page)
applepg = urlopen(apple_page)

# now we parse with beautifulsoup
soup = BeautifulSoup(page, 'html.parser')
applesoup = BeautifulSoup(applepg, 'html.parser')

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

# AAPL stock below
parentlist2 = []

applerow = []
row_box = applesoup.find('tr', attrs={'class': 'data-row21'})
for col in row_box.find_all('td'):
    coltext = col.get_text()
    applerow.append(coltext)
parentlist2.append(applerow)

applerow = []
row_box = applesoup.find('tr', attrs={'class': 'data-row22'})
for col in row_box.find_all('td'):
    coltext = col.get_text()
    applerow.append(coltext)
parentlist2.append(applerow)

applerow = []
row_box = applesoup.find('tr', attrs={'class': 'data-row23'})
for col in row_box.find_all('td'):
    coltext = col.get_text()
    applerow.append(coltext)
parentlist2.append(applerow)

applerow = []
row_box = applesoup.find('tr', attrs={'class': 'data-row24'})
for col in row_box.find_all('td'):
    coltext = col.get_text()
    applerow.append(coltext)
parentlist2.append(applerow)

applerow = []
row_box = applesoup.find('tr', attrs={'class': 'data-row25'})
for col in row_box.find_all('td'):
    coltext = col.get_text()
    applerow.append(coltext)
parentlist2.append(applerow)

applerow = []
row_box = applesoup.find('tr', attrs={'class': 'data-row26'})
for col in row_box.find_all('td'):
    coltext = col.get_text()
    applerow.append(coltext)
parentlist2.append(applerow)

for row in parentlist:
    try:
        labels = [row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10]]
        c.execute('INSERT INTO MSFTCallsJan2019 (ContractName, Date, Strike, LastPrice, Bid, Ask, Change, PChange, Volume, Openinterest, ImpliedVolatility) VALUES (?,?,?,?,?,?,?,?,?,?,?)', labels)
        #format(cn=row[0],dt=row[1],strike=row[2],lp=row[3],bid=row[4],ask=row[5],ch=row[6],pch=row[7],vol=row[8],oi=row[9],iv=row[10]))
    except sqlite3.IntegrityError:
        print('I don\'t have primary keys so this error shouldn\'t happen.')

for row in parentlist2:
    try:
        labels = [row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10]]
        c.execute('INSERT INTO AAPLCallsJan2019 (ContractName, Date, Strike, LastPrice, Bid, Ask, Change, PChange, Volume, Openinterest, ImpliedVolatility) VALUES (?,?,?,?,?,?,?,?,?,?,?)', labels)
        #format(cn=row[0],dt=row[1],strike=row[2],lp=row[3],bid=row[4],ask=row[5],ch=row[6],pch=row[7],vol=row[8],oi=row[9],iv=row[10]))
    except sqlite3.IntegrityError:
        print('I don\'t have primary keys so this error shouldn\'t happen.')

conn.commit()
conn.close()