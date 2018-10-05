import sqlite3
from flask import g, Flask, flash, redirect, render_template, request, session
import os
import datetime

DATABASE = './options.db'

app = Flask(__name__)

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route("/", methods=["GET", "POST"])
def index():
    db = get_db()
    cursor = db.execute('SELECT ContractName, Date, Strike, LastPrice FROM MSFTCallsJan2019')
    return render_template('index.html', items=cursor.fetchall())
