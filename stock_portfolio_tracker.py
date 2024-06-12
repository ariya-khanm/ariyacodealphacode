import requests
import pandas as pd

# Alpha Vantage API configuration
API_KEY = 'your_alpha_vantage_api_key'
BASE_URL = 'https://www.alphavantage.co/query'

# Portfolio dictionary to store stock data
portfolio = {}

def get_stock_data(symbol):
    """Fetch real-time stock data from Alpha Vantage API."""
    params = {
        'function': 'TIME_SERIES_INTRADAY',
        'symbol': symbol,
        'interval': '1min',
        'apikey': API_KEY
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()
    if 'Time Series (1min)' in data:
        latest_time = list(data['Time Series (1min)'].keys())[0]
        stock_info = data['Time Series (1min)'][latest_time]
        return {
            'symbol': symbol,
            'price': float(stock_info['1. open']),
            'time': latest_time
        }
    else:
        return None

def add_stock(symbol, shares):
    """Add a stock to the portfolio."""
    stock_data = get_stock_data(symbol)
    if stock_data:
        portfolio[symbol] = {
            'shares': shares,
            'price': stock_data['price']
        }
        print(f"Added {shares} shares of {symbol} at ${stock_data['price']:.2f}")
    else:
        print(f"Failed to retrieve data for {symbol}")

def remove_stock(symbol):
    """Remove a stock from the portfolio."""
    if symbol in portfolio:
        del portfolio[symbol]
        print(f"Removed {symbol} from portfolio")
    else:
        print(f"{symbol} not found in portfolio")

def calculate_portfolio_performance():
    """Calculate and print the performance of the portfolio."""
    total_value = 0
    for symbol, data in portfolio.items():
        stock_data = get_stock_data(symbol)
        if stock_data:
            current_price = stock_data['price']
            initial_price = data['price']
            shares = data['shares']
            value = shares * current_price
            total_value += value
            gain = (current_price - initial_price) * shares
            print(f"{symbol}: {shares} shares, Initial Price: ${initial_price:.2f}, Current Price: ${current_price:.2f}, Gain: ${gain:.2f}")
        else:
            print(f"Failed to retrieve current data for {symbol}")
    print(f"Total Portfolio Value: ${total_value:.2f}")

# Main logic
while True:
    print("\nStock Portfolio Tracker")
    print("1. Add stock")
    print("2. Remove stock")
    print("3. View portfolio performance")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        symbol = input("Enter stock symbol: ").upper()
        shares = int(input("Enter number of shares: "))
        add_stock(symbol, shares)
    elif choice == '2':
        symbol = input("Enter stock symbol to remove: ").upper()
        remove_stock(symbol)
    elif choice == '3':
        calculate_portfolio_performance()
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please try again.")