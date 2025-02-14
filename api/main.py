# insightease_forex/main.py
# Import insightease API Class
from insightease_stock import insighteaseStock


def main():
    # An API key, you can get free at https://insighteaseapi.com/dashboard
    stock_api = insighteaseStock(api_key='Your_api_key')

    stock_latest_price = stock_api.get_stock_Latest_price(country='united-states', exchange='NYSE')
    print("stock_latest_price:", stock_latest_price)

    stocks_indices = stock_api.get_stocks_indices(country="japan,turkey")
    stocks_indices = stock_api.get_stocks_indices(country="United-states")

    print("Stock List:", stocks_indices)

    # get stock list
    stock_list = stock_api.get_stocks_list(country="japan,turkey")
    stock_list = stock_api.get_stocks_list(sector="services,energy", country="japan,turkey")
    stock_list = stock_api.get_stocks_list(exchange='nyse,nasdaq,pari')
    print("Stock List:", stock_list)

    # get stock latest price
    stock_latest_price = stock_api.get_stock_Latest_price(country="japan,turkey")
    stock_latest_price = stock_api.get_stock_Latest_price(exchange='nyse,nasdaq,pari')
    stock_latest_price = stock_api.get_stock_Latest_price(symbol='AAPL', exchange='nasdaq,mexico')
    stock_latest_price = stock_api.get_stock_Latest_price(country='united-states', exchange='NYSE')

    print("stock_latest_price:", stock_latest_price)

    # get indicies latest

    indices_latest_price = stock_api.get_indices_latest(id='1')
    indices_latest_price = stock_api.get_indices_latest(id='1,2')
    indices_latest_price = stock_api.get_indices_latest(country="japan,turkey")
    indices_latest_price = stock_api.get_indices_latest(country="japan")
    print("stock_latest_price:", indices_latest_price)


    # Get Currency History
    history_data = stock_api.get_history({
        'id': '10',
        'period': '1d',
        'level': 1,
        'from': '2024-10-30',
        'to': '2024-10-31'
    })
    print("History Data for countries:", history_data)

    history_data = stock_api.get_history({
        'indices_id': '1',
        'period': '1d',
        'from': '2024-10-30',
        'to': '2024-10-31'
    })
    print("History Data for countries:", history_data)

    history_data = stock_api.get_history({
        'indices_id': '1',
        'period': '1d'
    })
    print("History Data for countries:", history_data)

    history_data = stock_api.get_history({
    'id': '3',
    'period': '1h'
    })
    print("History Data for countries:", history_data)

    # get stock dividend
    stock_dividend = stock_api.stock_dividend(id='1')
    stock_dividend = stock_api.stock_dividend(id='1,2')
    stock_dividend = stock_api.stock_dividend(symbol="AAPL")

    print("stock dividend:", stock_dividend)

    # get stock dividend
    stock_profile = stock_api.get_profile(id='1')
    stock_profile = stock_api.get_profile(id='1,2')
    stock_profile = stock_api.get_profile(symbol="TSLA")

    print("stock dividend:", stock_profile)

    # get performance
    performance = stock_api.get_performance(country='germany', sector='technology')
    performance = stock_api.get_performance(sector="services,energy")
    performance = stock_api.get_performance(exchange='nyse,nasdaq,pari')
    performance = stock_api.get_performance(indices_id='1,2,3')
    print("performance:", performance)

    # get fundamental
    fundamental = stock_api.get_fundamental(country='germany', sector='technology')
    fundamental = stock_api.get_fundamental(sector="services,energy")
    fundamental = stock_api.get_fundamental(exchange='nyse,nasdaq,pari')
    fundamental = stock_api.get_fundamental(indices_id='1,2,3')
    print("fundamental:", fundamental)

    # get stock income
    stock_income = stock_api.stock_income(symbol='AAPL')
    stock_income = stock_api.stock_income(id='1', duration='interim')
    print("Stock Income:", stock_income)

    stock_cash = stock_api.stock_cash(id='1')
    stock_cash = stock_api.stock_cash(id='1', duration='interim')
    print("Stock Income:", stock_cash)

    stock_balance = stock_api.stock_balance(id='1')
    stock_balance = stock_api.stock_balance(id='1', duration='interim')
    print("Stock Income:", stock_balance)

    # Earning does not support duration parameter
    stock_earning = stock_api.stock_earning(id='1')
    print("Stock Income:", stock_earning)

    # Get Pivot Points
    pivot_points = stock_api.get_pivot_points(id="4", period='1d')
    pivot_points = stock_api.get_pivot_points(symbol="IBM", period="1d")

    print("Pivot Points:", pivot_points)

    # Get Moving Averages
    moving_averages = stock_api.get_moving_averages(id="4", period='1d')
    moving_averages = stock_api.get_moving_averages(symbol="IBM", period='1d')
    print("Moving Averages:", moving_averages)

    # Get Technical Indicators

    indicators = stock_api.get_technical_indicator(symbol='7', period='1d')
    indicators = stock_api.get_technical_indicator(symbol="IBM,AV", period='1d')
    print("Technical Indicators:", indicators)

    # Get signals indicator

    signals_indicator = stock_api.get_signals_indicator(symbol="TSLA", indices_id="MSFT", index_id="FB")
    signals_indicator = stock_api.get_signals_indicator(id='1,2,3,4,5')
    signals_indicator = stock_api.get_signals_indicator(country='germany')
    print("Technical Indicators:", signals_indicator)

    # Search API
    search_results = stock_api.get_search_query("General Electric")
    search_results = stock_api.get_search_query(search='eneral Electric', strict=0, type='index')
    print("Search Results: ", search_results)

    country_report = stock_api.get_country_report()
    print("Search Results: ", country_report)


if __name__ == "__main__":
    main()
