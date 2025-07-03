import sqlite3
import yfinance as yf

#my protfolio stocks
TICKERS = {
    "AAPL": "Apple Inc.",
    "MSFT": "Microsoft Corporation",
    "GOOGL": "Alphabet Inc.",
    "NVDA": "NVIDIA Corporation",
    "AMZN": "Amazon.com Inc.",
    "META": "Meta Platforms Inc."
}

SECTOR_INFO = {
    "AAPL": "Technology",
    "MSFT": "Technology",
    "GOOGL": "Communication Services",
    "NVDA": "Semiconductors",
    "AMZN": "Consumer Discretionary",
    "META": "Communication Services"
}


conn = sqlite3.connect('stocks.db')
cursor = conn.cursor()


cursor.execute("DELETE FROM stocks")


for symbol, company in TICKERS.items():
    stock = yf.Ticker(symbol)
    info = stock.info

    try:
        current_price = info.get("currentPrice")
        high_52w = info.get("fiftyTwoWeekHigh")
        low_52w = info.get("fiftyTwoWeekLow")
        change_percent = info.get("regularMarketChangePercent")
        dividend = info.get("dividendRate") or 0.0
        eps = info.get("trailingEps")
        pe_ratio = info.get("trailingPE")
        sector = SECTOR_INFO.get(symbol, "Unknown")

        cursor.execute('''
            INSERT INTO stocks (
                symbol, company, sector, current_price,
                "52w_high", "52w_low", change_percent,
                dividend, eps, pe_ratio
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            symbol, company, sector, current_price,
            high_52w, low_52w, change_percent,
            dividend, eps, pe_ratio
        ))

        print(f" {symbol} added.")

    except Exception as e:
        print(f" {symbol} error: {e}")

conn.commit()
conn.close()
print(" every company data added")
