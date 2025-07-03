import yfinance as yf

def fetch_stock_data(symbol, company, sector):
    try:
        ticker = yf.Ticker(symbol)
        fast = = ticker.fast_info

        return {
            'symbol': symbol,
            'company': company,
            'sector': sector,
            'current_price': info.get('currentPrice', 'N/A'),
            '52w_high': info.get('fiftyTwoWeekHigh', 'N/A'),
            '52w_low': info.get('fiftyTwoWeekLow', 'N/A'),
            'change_percent': info.get('regularMarketChangePercent', 'N/A'),
            'dividend': info.get('dividendRate', 'N/A'),
            'eps': info.get('epsTrailingTwelveMonths', 'N/A'),
            'pe_ratio': info.get('trailingPE', 'N/A')
        }
    except Exception as e:
        return {
            'symbol': symbol,
            'company': company,
            'sector': sector,
            'error': str(e)
        }
