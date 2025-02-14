# InsightEase Stock API Wrapper

## Overview
This project provides a Python-based wrapper for interacting with the **InsightEase Stock API**. It allows users to fetch real-time stock market data, historical trends, financial reports, technical indicators, and more.

## Features
- Fetch **latest stock prices** for different exchanges (NYSE, NASDAQ, etc.).
- Retrieve **stock indices** from multiple countries.
- Access **historical stock data**.
- Fetch **stock dividends** and **company profiles**.
- Get **performance and fundamental analysis** of stocks.
- Retrieve **financial reports** (income, cash flow, balance sheet, earnings).
- Obtain **technical indicators** such as pivot points, moving averages, and trading signals.
- Perform **stock search queries**.
- Fetch **country-specific stock analytics reports**.

## Installation
To use this project, clone the repository and install dependencies:
```sh
$ git clone https://github.com/your-repo/insightease-stock-api.git
$ cd insightease-stock-api
$ pip install -r requirements.txt
```

## Usage
### 1. Set Up Your API Key
You need an API key from [InsightEase API](https://insighteaseapi.com/dashboard). Update `main.py` with your key:
```python
stock_api = insighteaseStock(api_key='YOUR_API_KEY')
```

### 2. Running the Main Script
Execute the script to fetch stock data:
```sh
$ python main.py
```

### 3. Example API Calls
#### Fetch Latest Stock Prices
```python
stock_latest_price = stock_api.get_stock_Latest_price(country='united-states', exchange='NYSE')
print(stock_latest_price)
```
#### Fetch Stock Indices
```python
indices = stock_api.get_stocks_indices(country='japan,turkey')
print(indices)
```
#### Fetch Historical Data
```python
history = stock_api.get_history({
    'id': '10',
    'period': '1d',
    'from': '2024-10-30',
    'to': '2024-10-31'
})
print(history)
```

## Project Structure
```
insightease-stock-api/
│-- main.py                # Main script to run API calls
│-- insightease_stock.py   # API wrapper class
│-- README.md              # Documentation
│-- requirements.txt       # Dependencies
```

## Dependencies
- Python 3.x
- `requests` (for API calls)

Install dependencies using:
```sh
$ pip install -r requirements.txt
```

## License
This project is licensed under the MIT License.

## Contributing
Feel free to fork this project and submit pull requests for improvements!

## Contact
For questions or support, contact [your-email@example.com].

