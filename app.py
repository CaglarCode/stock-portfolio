from flask import Flask, render_template
import sqlite3

app = Flask(__name__)
DATABASE = 'stocks.db'

def get_stock_data():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM stocks")
    data = cursor.fetchall()
    conn.close()
    return data

@app.route('/')
def index():
    stocks = get_stock_data()
    return render_template('index.html', stocks=stocks)

if __name__ == '__main__':
    app.run(debug=True)
