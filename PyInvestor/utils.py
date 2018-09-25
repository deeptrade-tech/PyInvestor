"""
__author__ = Fabio Capela

"""
import requests
import pandas as pd



IEX_URL = "https://api.iextrading.com/1.0" # the universal link to get access to the endpoint
time_columns = ["openTime","closeTime", "latestUpdate", "iexLastUpdated", "delayedPriceTime",
                "extendedPriceTime"]    # all the columns that have a timestamp


def _endpoint(key, symbol, endpoint, **kwargs):
    """ returns the json related to a particular endpoint. key corresponds to the differents location of the API endpoints.
    """
    request_url = "%s/%s/%s/%s"%(IEX_URL, key, symbol, endpoint)
    response =  requests.get(request_url, **kwargs)
    return response.json()

def _todatedf(df):
    for col in cols:
        
