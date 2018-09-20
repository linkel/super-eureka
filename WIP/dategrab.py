from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv
from datetime import datetime
import sqlite3
import re
from json import loads

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

# grab the text of the script that also contains the text "root.App.main"
# https://stackoverflow.com/questions/2580507/using-beautifulsoups-findall-to-search-html-elements-innertext-to-get-same-res
# https://stackoverflow.com/questions/866000/using-beautifulsoup-to-find-a-html-tag-that-contains-certain-text
script = soup.find("script", text=re.compile('root.App.main')).text
# use regex to get just the relevant part of the json - https://docs.python.org/3/library/re.html
# the regex translates to: find the string "\"expirationDates\":[" and grab everything (.*) 
# period means match any character and * means match as many character as necessary until you hit 
# the first ] (? means match the first)
# test it out here - regexr.com/3vqka
expirationDates = re.search("{\"expirationDates\":\[.*?\]", script).group(0) + "}"
# decode the json - https://docs.python.org/2/library/json.html
dates = loads(expirationDates)
# use it like this:
print(dates['expirationDates'])
