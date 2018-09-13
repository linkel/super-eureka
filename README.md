# super-eureka

## Background
All I wanted was some $MSFT call option price data. I wanted to know the prices for December 2018 calls with strikes at 105, 110, and 115. But I didn't want to enter it into an Excel file by hand, and I also didn't want to be glued to the screen staring at a browser or peeking at Robinhood on my phone all day. 

Instead, I want to be glued to the screen staring at VSCode! Hurray--a major quality of life improvement. 

Super-Eureka is a Python script that uses BeautifulSoup4 to scrape $MSFT call options from Yahoo. It saves the last price, bid/ask, IV, and more into a sqlite3 database. This makes it possible to perform SQL queries on the data and down the line, plot the price of an option over time! Yes, very simple, but even the small things in life are worth enjoying.

## Changelog
### Version 0.0.1
- 2018-09-13 - SQLite3 online.
- 2018-09-12 - Scraper is scraping. Poops into a CSV file.