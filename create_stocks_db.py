# create_stocks_db.py
import sqlite3
import pandas as pd

# Excel dosyasını oku
df = pd.read_excel("Stock Tracker.xlsx", sheet_name="Sheet1")

# SQLite veritabanını oluştur
conn = sqlite3.connect("stocks.db")
cursor = conn.cursor()

# Tabloyu oluştur
cursor.execute("DROP TABLE IF EXISTS stocks")
cursor.execute("""
CREATE TABLE stocks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    symbol TEXT NOT NULL,
    company TEXT NOT NULL,
    sector TEXT
)
""")

# Gerekli verileri al ve ekle
stock_data = df[['Symbol', 'Company', 'Sector']].dropna().values.tolist()
cursor.executemany("INSERT INTO stocks (symbol, company, sector) VALUES (?, ?, ?)", stock_data)

conn.commit()
conn.close()
print("stocks.db başarıyla oluşturuldu ve veriler yüklendi.")