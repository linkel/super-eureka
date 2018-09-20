import sqlite3
import numpy as np
import matplotlib.pyplot as plt
from dateutil import parser
import sys

tablepath = sys.argv[1]
strikeprice = sys.argv[2]

conn = sqlite3.connect('options.db')
c = conn.cursor()
datenow = []
lastprice = []

try:
    # the "safe" way of doing this doesn't allow modifying the table, so alas
    for row in c.execute("SELECT * FROM %s WHERE Strike=%s" % (tablepath, strikeprice)):
        datenow.append(parser.parse(row[1]))
        print(parser.parse(row[1]))
        lastprice.append(row[3])
except sqlite3.OperationalError:
    print("{} does not exist. Check your db for the exact table name.".format(tablepath))
print(datenow)
print(lastprice)
plt.plot(datenow,lastprice, 'ro:')
plt.show()
