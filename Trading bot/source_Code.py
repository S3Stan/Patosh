# Imports



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
def return_api_key():
    return API_KEY



