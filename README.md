# Stock API Python by Insightease

## Overview
This project integrates seamlessly with the **[Stock API Python - Insightease](https://insightease.com/docs/stock-api)** to retrieve and process stock market data. It offers a range of functionalities, including fetching stock symbols, retrieving real-time prices, analyzing historical data, and generating financial reports—all powered by Python.

### Components:
- `insightease_stock.py`: Implements the `insighteaseStock` class, which provides multiple API interaction methods.
- `main.py`: Demonstrates the usage of `insighteaseStock` by calling various functions and printing the results.

# Integration of the Insightease Stock API

## Summary
Insightease's Stock API provides features such as stock price retrieval, accessing the latest market values, fetching stock symbols, and leveraging Python to analyze historical data.

### Elements:
- The `insighteaseStock` class, which offers a number of API interaction methods, is implemented by `insightease_stock.py`.
- `main.py`: Shows how to use `insighteaseStock` by executing different functions and displaying the output.

## Installation

### Necessities
Make sure Python is installed; it is advised to use Python 3.6 or later. Install the necessary dependencies next:

#### Necessary Library
**Requests**: Making HTTP calls to the API and managing their answers are done with this library.

Use the following command to install the dependencies:
```sh
pip install requests
```

## Application
To make API requests and retrieve stock data, run the main script:
```sh
python main.py
```

## Use Case Example
An example request to retrieve the most recent Apple (AAPL) stock price is as follows:
```python
from insightease_stock import insighteaseStock

stock_api = insighteaseStock(api_key='YOUR_API_KEY')
latest_price = stock_api.get_stock_Latest_price(symbol='AAPL', exchange='NASDAQ')
print("Latest Price of AAPL:", latest_price)
```
# Extract Exchange Data
## Outout
| Exchange Name     | Exchange Name     | Exchange Name     | Exchange Name     |
|-------------------|-------------------|-------------------|-------------------|
| Tokyo             | NASDAQ            | Shenzhen          | NYSE              |
| KOSDAQ            | Shanghai          | London            | BSE               |
| Hong Kong         | BM&FBovespa       | Thailand          | Kuala Lumpur      |
| Stockholm         | Paris             | Jakarta           | Seoul             |
| Frankfurt         | Moscow            | Toronto           | TSXV              |
| Singapore         | OTC Markets       | NSE               | Mexico            |
| Istanbul          | Karachi           | Johannesburg      | Xetra             |
| Philippines       | Switzerland       | Saudi Arabia      | Madrid            |
| Berlin            | NYSE Amex         | Helsinki          | Copenhagen        |
| Amsterdam         | BIVA              | Spotlight         | Taiwan            |
| Abu Dhabi         | NGM               | Dubai             | Ireland           |
| Brussels          | Dusseldorf        | B3                | CSE               |
| SOMA              | Iceland           | LATIBEX           | Hamburg           |
| Oslo              | Sydney            | Lisbon            | TradeGate         |
| Milan             | Egypt             | BATS Europe       | NEO               |
| Munich            | Ho Chi Minh       | Stuttgart         | KONEX             |
| CBOE Canada       | Luxembourg        |                   |                   |


    

## Notes
- In order to manage API calls, the **requests** library is necessary.
- Rather than being hardcoded, the API key ought to be safely stored.
- Verify that the API base URL is accurate and current.
- Since the return format is JSON, processing and parsing must be done correctly.

### 🔗 Other Links
- **Stock Documentation:** [Stock Documentation](https://insightease.com/docs/stock-api#api-documentation)
- **Contact Us:** [Website](https://insightease.com)

## Permit
The goal of this endeavor is education. For usage restrictions, please refer to the terms provided by the API provider.

