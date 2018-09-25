"""
__author__ = Fabio Capela

"""
import requests
import pandas as pd



IEX_URL = "https://api.iextrading.com/1.0" # the universal link to get access to the endpoint
time_columns = ["openTime","closeTime", "latestUpdate", "iexLastUpdated", "delayedPriceTime",
                "extendedPriceTime", "lastUpdated"]    # all the columns that have a timestamp
timerange_split = ['5y', '2y', '1y', 'ytd', '6m', '3m', '1m']  # time range for the splits 
timerange_chart = ['5y', '2y', '1y', 'ytd', '6m', '3m', '1m', '1d', 'date', 'dynamic']  # time range for the timeseries/charts



def _endpoint(key, symbol, endpoint, **kwargs):
    """ returns the json related to a particular endpoint. key corresponds to the differents location of the API endpoints.
    """
    request_url = "%s/%s/%s/%s"%(IEX_URL, key, symbol, endpoint)
    response =  requests.get(request_url, **kwargs)
    return response.json()


def _correctdate(df):
    for col in time_columns:
        if col in df.columns:
            df[col] = pd.to_datetime(df[col], unit='ms')
        
