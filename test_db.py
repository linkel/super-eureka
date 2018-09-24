import sqlite3
def testDbConnect():
    conn = sqlite3.connect('options.db')
    c = conn.cursor()

    # check that db connection works and that row exists
    try:
        for row in c.execute("SELECT * FROM MSFTCalls WHERE Strike=110"):
            assert row
    except sqlite3.OperationalError:
        print("{} does not exist. Check your db for the exact table name.".format(tablepath))