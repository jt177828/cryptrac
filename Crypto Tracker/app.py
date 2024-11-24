import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Function to fetch and display crypto data
def fetch_crypto_data(ticker, period='7d', interval='1h'):
    """
    Fetch cryptocurrency data using yfinance.
    Args:
        ticker (str): Cryptocurrency ticker symbol (e.g., 'BTC-USD').
        period (str): Period for historical data (e.g., '7d', '1mo', '1y').
        interval (str): Data interval (e.g., '1h', '1d').
    Returns:
        DataFrame: Historical cryptocurrency data.
    """
    crypto = yf.Ticker(ticker)
    data = crypto.history(period=period, interval=interval)
    if data.empty:
        print(f"No data found for {ticker}. Check the ticker symbol.")
        return None
    return data

# Function to plot crypto data
def plot_crypto_data(data, ticker):
    """
    Plot cryptocurrency data.
    Args:
        data (DataFrame): Historical cryptocurrency data.
        ticker (str): Cryptocurrency ticker symbol.
    """
    plt.figure(figsize=(10, 5))
    plt.plot(data.index, data['Close'], label=f"{ticker} Closing Price")
    plt.title(f"{ticker} Price History")
    plt.xlabel("Date")
    plt.ylabel("Price (USD)")
    plt.legend()
    plt.grid()
    plt.show()

# Main tracker functionality
def crypto_tracker():
    print("Crypto Tracker with yfinance")
    ticker = input("Enter the cryptocurrency ticker (e.g., 'BTC-USD'): ").strip()
    period = input("Enter the data period (e.g., '7d', '1mo', '1y'): ").strip() or '7d'
    interval = input("Enter the data interval (e.g., '1h', '1d'): ").strip() or '1h'
    
    data = fetch_crypto_data(ticker, period, interval)
    if data is not None:
        print(data.tail())  # Show the last few rows of data
        plot_crypto_data(data, ticker)

# Run the tracker
if __name__ == "__main__":
    crypto_tracker()
