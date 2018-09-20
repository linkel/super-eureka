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
ctr = 0

while ctr < 38:
    onerow =[]
    MSFTrow = "data-row" + str(ctr)
    row_box = soup.find('tr', attrs={'class': MSFTrow})
    try:
        for col in row_box.find_all('td'):
            coltext = col.get_text()
            onerow.append(coltext)
        parentlist.append(onerow)
    except AttributeError:
        print("Nonetype object at row " + str(ctr))
    ctr += 1

# AAPL stock below
parentlist2 = []
AAPLctr = 0

while AAPLctr < 74:
    applerow = []
    AAPLrow = "data-row" + str(AAPLctr)
    row_box = applesoup.find('tr', attrs={'class': AAPLrow})
    try:
        for col in row_box.find_all('td'):
            coltext = col.get_text()
            applerow.append(coltext)
        parentlist2.append(applerow)
    except AttributeError:
        print("Nonetype object at row " + str(AAPLctr))
    AAPLctr += 1
    # print(AAPLctr)

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