import unittest
import pandas as pd
from pandas.testing import assert_frame_equal
from unittest.mock import patch
import yfinance as yf

# Assuming the functions are in a module named finance_module
from src.data_preprocessing.data_processing import fetch_data, clean_data

class TestFinanceModule(unittest.TestCase):

    @patch('yfinance.download')
    def test_fetch_data(self, mock_download):
        # Mock data
        mock_data = pd.DataFrame({
            'Open': [100, 101],
            'High': [102, 103],
            'Low': [99, 100],
            'Close': [101, 102],
            'Volume': [1000, 1100],
            'Adj Close': [101, 102]
        })
        mock_download.return_value = mock_data

        tickers = ['AAPL']
        start = '2020-01-01'
        end = '2020-01-02'
        expected_data = {'AAPL': mock_data}

        result = fetch_data(tickers, start, end)
        assert_frame_equal(result['AAPL'], expected_data['AAPL'])

    def test_clean_data(self):
        # Data with missing values
        data = pd.DataFrame({
            'Open': [100, None],
            'High': [102, 103],
            'Low': [99, 100],
            'Close': [101, None],
            'Volume': [1000, 1100],
            'Adj Close': [101, 102]
        })
        expected_cleaned_data = data.dropna()

        result = clean_data(data)
        assert_frame_equal(result, expected_cleaned_data)

if __name__ == '__main__':
    unittest.main()
