import sqlite3


conn = sqlite3.connect('stocks.db')
cursor = conn.cursor()


cursor.execute('''
CREATE TABLE IF NOT EXISTS stocks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    symbol TEXT,
    company TEXT,
    sector TEXT,
    current_price REAL,
    "52w_high" REAL,
    "52w_low" REAL,
    change_percent REAL,
    dividend REAL,
    eps REAL,
    pe_ratio REAL
)
''')


sample_data = [
    ('AAPL', 'Apple Inc.', 'Technology', 210.12, 220.00, 150.00, 1.25, 0.88, 5.62, 22.3),
    ('GOOGL', 'Alphabet Inc.', 'Communication Services', 135.55, 145.00, 95.00, -0.42, 0.00, 4.20, 30.5),
    ('MSFT', 'Microsoft Corp.', 'Technology', 360.77, 370.00, 250.00, 0.67, 1.25, 7.33, 31.2)
]

cursor.executemany('''
INSERT INTO stocks (
    symbol, company, sector, current_price,
    "52w_high", "52w_low", change_percent,
    dividend, eps, pe_ratio
) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
''', sample_data)

conn.commit()
conn.close()
print("datase created")
