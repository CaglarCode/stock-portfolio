Stock Portfolio Tracker

This is a simple web application built with Flask that displays a portfolio of stocks with real-time data. It uses yfinance to fetch dynamic stock data and SQLite as a local database to store basic company information.

Features
	•	Displays stock symbol, company name, sector
	•	Fetches current price, 52-week high/low, EPS, P/E ratio, and dividend data dynamically
	•	Uses Bootstrap for a clean and responsive UI

Technologies Used
	•	Flask
	•	SQLite
	•	yfinance
	•	Bootstrap
	•	Gunicorn 

Folder Structure

stock-portfolio/
├── app.py
├── fetch_data.py
├── create_database.py
├── stocks.db
├── requirements.txt
├── render.yaml
├── README.md
├── templates/
│   ├── base.html
│   └── index.html
├── static/
│   └── style.css


Running Locally

1. Install dependencies
pip install -r requirements.txt

2. Create the database (only once)
python create_database.py

3. Fetch live data from Yahoo Finance
python fetch_data.py

4. Run the Flask app
python app.py

Go to http://localhost:5000 to view the app.

Deployment

This project can be deployed on Render using the render.yaml file and Gunicorn as the WSGI server.



Note: This project was created for academic purposes. 
