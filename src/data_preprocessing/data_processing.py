import yfinance as yf
import pandas as pd

def fetch_data(tickers, start, end):
    """
    Fetch historical financial data for specified tickers and date range using yfinance.
    """
    data = {}
    for ticker in tickers:
        df = yf.download(ticker, start=start, end=end)
        data[ticker] = df[['Open', 'High', 'Low', 'Close', 'Volume', 'Adj Close']]
    return data

def clean_data(df):
    """
    Clean the given DataFrame by dropping rows with missing values.
    """
    df = df.dropna()
    return df
