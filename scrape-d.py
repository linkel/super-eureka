from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv
from datetime import datetime
import sqlite3

# this version of scrape will prompt for the call expiry you're interested in
# not currently functioning, just a placeholder

conn = sqlite3.connect('options.db')

c = conn.cursor()

# somehow I am unable to select the option and select tag using beautiful soup. It's invisible? 
# I don't want to do it so manually like this...

# variable for url
nov16 = "https://finance.yahoo.com/quote/MSFT/options?date=1542326400"
dec12 = "https://finance.yahoo.com/quote/MSFT/options?date=1545350400"
jan18 = "https://finance.yahoo.com/quote/MSFT/options?date=1547769600"
apr18 = "https://finance.yahoo.com/quote/MSFT/options?date=1555545600"

print("1. Nov 16, 2018")
print("2. Dec 12, 2018")
print("3. Jan 18, 2019")
print("4. Apr 18, 2019")

answer = input('What expiry date are you interested in?')
# add checks to make sure only input is 1 - 4
quote_page = # decided by user input
# query the website and return the html to the variable page
page = urlopen(quote_page)

# now we parse with beautifulsoup
soup = BeautifulSoup(page, 'html.parser')



