# Imports
from datetime import datetime


# Data input and API connections:

## 1 - Latest rate endpoint
API_KEY = '3b77809c36c4efa417e527324a9ec241'

latest_rates_endpoint = 'https://api.currencylayer.com/live'

## 2 - Historical rates
histo_rates_endpoint = 'https://api.currencylayer.com/historical?date=YYYY-MM-DD'


## 3 - Time-series data
timr_frame_endpoint = 'https://api.currencylayer.com/timeframe?start_date=2015-01-01&end_date=2015-05-01'


# functions

# return api key to front end ## << find a way to encode it>>
def return_api_access_key():
    return API_KEY


# Return live price updates..
def get_live_price_update(single_base_pair, currency_pair_list):
    endpoint = str('live')
    data_url = f'http://api.currencylayer.com/{endpoint}?access_key={return_api_access_key()}&source={single_base_pair}'#&source={currency_pair_list}'#&format=1'
    return data_url # return to notebook frontend.


# Return the historical price updates
def get_historical_price_update(day_date):
    endpoint = str('historical')
    data_pack = f'http://api.currencylayer.com/{endpoint}?access_key={return_api_access_key()}&date={day_date}'
    return data_pack # return data packet to the front end
    

# 
def get_time_series_data(currency, start_date, end_date):
    endpoint = str('timeframe') 
    data_pack = f'http://api.currencylayer.com/{endpoint}?access_key={return_api_access_key()}&source={currency}&start_date={start_date}&end_date={end_date}'#start_date={start_date}&end_date={end_date}'
    #print(data_pack)
    
    return data_pack # return data packet to the front end 




# https://api.currencylayer.com/historical?date=YYYY-MM-DD
# https://api.currencylayer.com/timeframe?start_date=2015-01-01&end_date=2015-05-01

# url = f'http://api.currencylayer.com/{endpoint}?access_key={access_key}&source={base_currency}'#&currencies={trade_currency_list}'#&format=1'
# url1 = f'https://api.exchangeratesapi.io/v1/{endpoint}?access_key={access_key}'
