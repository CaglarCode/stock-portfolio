from flask import Flask, render_template
import sqlite3
from stocks import fetch_stock_data

app = Flask(__name__)

DB_PATH = 'stocks.db'

@app.route('/')
def index():
   
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT symbol, company, sector FROM stocks")
    stocks = cursor.fetchall()
    conn.close()

    
    stock_data = [fetch_stock_data(symbol, company, sector) for symbol, company, sector in stocks]

    return render_template('index.html', stocks=stock_data)

if __name__ == '__main__':
    app.run(debug=True)
