import sqlite3


stock_data = [
    ("ASML", "ASML Holding NV", "AI Chips"),
    ("META", "Meta Platforms Inc", "Big Tech"),
    ("ISRG", "Intuitive Surgical Inc", "MedTech"),
    ("ADBE", "Adobe Inc", "Software"),
    ("MSFT", "Microsoft Corp", "Big Tech")
]


conn = sqlite3.connect("stocks.db")
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS stocks")
cursor.execute("""
CREATE TABLE stocks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    symbol TEXT NOT NULL,
    company TEXT NOT NULL,
    sector TEXT
)
""")

cursor.executemany("INSERT INTO stocks (symbol, company, sector) VALUES (?, ?, ?)", stock_data)

conn.commit()
conn.close()

print(" stocks.db created ")
