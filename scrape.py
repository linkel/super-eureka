from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv
from datetime import datetime
import sqlite3

conn = sqlite3.connect('options.db')

c = conn.cursor()

# variable for url
quote_page = 'https://finance.yahoo.com/quote/MSFT/options?date=1545350400'
apple_page = 'https://finance.yahoo.com/quote/AAPL/options?date=1545350400'

# query the website and return the html to the variable page
page = urlopen(quote_page)
applepg = urlopen(apple_page)

# now we parse with beautifulsoup
soup = BeautifulSoup(page, 'html.parser')
applesoup = BeautifulSoup(applepg, 'html.parser')

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

#with open('index.csv', 'a') as csv_file:
#    writer = csv.writer(csv_file)
#    for row in parentlist:
#        writer.writerow(row)

for row in parentlist:
    try:
        labels = [row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10]]
        c.execute('INSERT INTO MSFTCalls (ContractName, Date, Strike, LastPrice, Bid, Ask, Change, PChange, Volume, Openinterest, ImpliedVolatility) VALUES (?,?,?,?,?,?,?,?,?,?,?)', labels)
        #format(cn=row[0],dt=row[1],strike=row[2],lp=row[3],bid=row[4],ask=row[5],ch=row[6],pch=row[7],vol=row[8],oi=row[9],iv=row[10]))
    except sqlite3.IntegrityError:
        print('I don\'t have primary keys so this error shouldn\'t happen.')

for row in parentlist2:
    try:
        labels = [row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10]]
        c.execute('INSERT INTO AAPLCalls (ContractName, Date, Strike, LastPrice, Bid, Ask, Change, PChange, Volume, Openinterest, ImpliedVolatility) VALUES (?,?,?,?,?,?,?,?,?,?,?)', labels)
        #format(cn=row[0],dt=row[1],strike=row[2],lp=row[3],bid=row[4],ask=row[5],ch=row[6],pch=row[7],vol=row[8],oi=row[9],iv=row[10]))
    except sqlite3.IntegrityError:
        print('I don\'t have primary keys so this error shouldn\'t happen.')

conn.commit()
conn.close()