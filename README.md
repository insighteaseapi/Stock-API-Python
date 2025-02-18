# Stock API Python by Insightease

## Overview
This project integrates seamlessly with the **[Stock API Python by Insightease](https://insightease.com/docs/stock-api)** to retrieve and process stock market data. It offers a range of functionalities, including fetching stock symbols, retrieving real-time prices, analyzing historical data, and generating financial reports—all powered by Python.

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
# Code to Extract Exchange Data
import requests

# Your API URL with the provided API key
url = "https://api.insightease.com/stock/analytics?api_key=Your_api_key"

- Send GET request to the API
response = requests.get(url)

- Check if the response is successful
if response.status_code == 200:
     Parse the response JSON
    data = response.json()
    
     Extract exchanges data
    exchanges = data.get('response', {}).get('exchanges', {})
    
     Print the exchanges
    if exchanges:
        print("Exchanges of countries:")
        for exchange, count in exchanges.items():
            print(f"{exchange}: {count}")
    else:
        print("No exchange data found.")
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")

    
## Outout
  **Exchanges of countries:**
- Tokyo: 4075
- NASDAQ: 4061
- Shenzhen: 2548
- NYSE: 2374
- KOSDAQ: 1701
- Shanghai: 1599
- London: 1318
- BSE: 1269
- Hong Kong: 1244
- BM&FBovespa: 1143

    

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

