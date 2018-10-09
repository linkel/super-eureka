# super-eureka

## Background
All I wanted was some $MSFT call option price data. I wanted to know the prices for December 2018 calls with strikes at 105, 110, and 115. But I didn't want to enter it into an Excel file by hand, and I also didn't want to be glued to the screen staring at a browser or peeking at Robinhood on my phone all day. 

Instead, I want to be glued to the screen staring at VSCode! Hurray--a major quality of life improvement. 

Super-Eureka is a Python script that uses BeautifulSoup4 to scrape $MSFT call options from Yahoo. It saves the last price, bid/ask, IV, and more into a sqlite3 database. This makes it possible to perform SQL queries on the data and plot the price of an option over time! Yes, very simple, but even the small things in life are worth enjoying.

## Usage
Scraper currently scrapes both MSFT and AAPL call options near the money and has one fixed expiry date it looks at. Plotter takes two parameters: the table and the strike price. 

`python scraper.py`

`python plotter.py MSFTCallsJan2019 105`

## Changelog
### Version 0.0.2
- 2018-10-08 - Now shows a dropdown menu, enabling selection of which table to view.
- 2018-10-05 - Added Flask app, displays just one table in the browser.
- 2018-09-26 - Created copies of the main script to pull Jan and Apr 2019 calls.
### Version 0.0.1
- 2018-09-20 - scrape.py now grabs information on all the strike prices instead of just the ones near the money
- 2018-09-19 - Added support for scraping Jan 2019 calls.
- 2018-09-14 - plotter.py successfully plots data.
- 2018-09-13 - SQLite3 online.
- 2018-09-12 - Scraper is scraping. Plops data into a CSV file.

## To Do
- [x] Scrape calls that are not near the money as well.
- [x] Allow selection of which expiry dates to plot in plotter.py (limited)
- [ ] Allow user input on selection of expiry dates to scrape.
- [ ] Scrape puts. 
- [ ] Allow plotting volume and IV.
- [x] Display a table in the browser using Flask as the backend controller.
- [x] Create a dropdown menu to select different tables in the browser.
- [ ] Render my plots in the browser above the table info.
- [ ] Make the homepage more aesthetic Part 1.
