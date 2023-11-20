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



# Specify the API endpoint URL
# currencies = ['EUR', 'AUD', 'GBP', 'CNY', 'NZD']
# format = 'json'


# # Set endpoint and your access key
# endpoint = str('live')
# access_key =  source_Code.return_api_key()  # Replace 'API_KEY' with your actual access key
# base_currency = str('EUR')
# trade_currency_list = ['USD', 'AUD']


def get_live_price_update(single_base_pair, optional_param='currency_pair_list'):
    endpoint = str('live')
    access_key = return_api_key()
    data_url = f'http://api.currencylayer.com/{endpoint}?access_key={access_key}&source={single_base_pair}'#&currencies={trade_currency_list}'#&format=1'
    
    return data_url # return to notebook frontend.
    

# url = f'http://api.currencylayer.com/{endpoint}?access_key={access_key}&source={base_currency}'#&currencies={trade_currency_list}'#&format=1'
# url1 = f'https://api.exchangeratesapi.io/v1/{endpoint}?access_key={access_key}'
