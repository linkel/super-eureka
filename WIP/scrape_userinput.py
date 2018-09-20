# A preliminary attempt at enabling user input of call expiries they want to scrape
# Thinking about it though, wouldn't the user always want to grab all of them?
# So perhaps this interface will be instead for the plotting portion, to select which to plot.

from urllib.request import urlopen
from bs4 import BeautifulSoup
from datetime import datetime
import sqlite3
import re
from json import loads

conn = sqlite3.connect('options.db')

c = conn.cursor()

dateArray = [1537488000, 1538092800, 1538697600, 1539302400, 1539907200, 1540512000, 1541116800, 1542326400, 1545350400, 1547769600, 1555545600, 1561075200, 1579219200, 1592524800, 1610668800]

counter = 0
for date in dateArray:
    print(counter, end='. ')
    print(datetime.utcfromtimestamp(date).strftime('%Y-%m-%d'))
    counter += 1

try:
    userChoice = int(input("Enter the number of the call expiry you would like to scrape. "))
except ValueError:
    print("Please type an integer.")

try:
    chosen = dateArray[userChoice]
    print("You have selected " + datetime.utcfromtimestamp(chosen).strftime('%Y-%m-%d') +".")
except IndexError:
    print("Please make sure your number is in range.")

quote_page = ('https://finance.yahoo.com/quote/MSFT/options?date=' + str(chosen))
print(quote_page)

