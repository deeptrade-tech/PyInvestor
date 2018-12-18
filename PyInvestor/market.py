from utils import IEX_URL, _endpointmarket, _correctdate
import requests
import pandas as pd
from pandas.io.json import json_normalize


"""
#########################################
/!\ Still needs to do the batch querying
#########################################
"""

                
def Crypto():
    """ returns an array of quotes for all cryptocurrencies supported by the IEX API. 
    """
    response = _endpointmarket('crypto')
    df = pd.DataFrame(response)
    _correctdate(df)
    return df


    
def UpcomingIPO():
    """ list of upcoming IPOs scheduled for the current
    and next month. The response has to
    """
    response = _endpointmarket('upcoming-ipos')
    rawData = response['rawData']
    viewData = response['viewData']
    df_raw = pd.DataFrame(rawData) # you have to take out some rows
    df_view =  pd.DataFrame(viewData)
    _correctdate(df_raw)
    _correctdate(df_view)
    return df_raw, df_view



def TodayIPO():
    """ list of today IPOs scheduled for the current
    and next month. The response has to
    """
    response = _endpointmarket('today-ipos')
    rawData = response['rawData']
    viewData = response['viewData']
    df_raw = pd.DataFrame(rawData) # you have to take out some rows
    df_view =  pd.DataFrame(viewData)
    _correctdate(df_raw)
    _correctdate(df_view)
    return df_raw, df_view



def Gainers():
    """ Biggest gainers in the market
    """
    response = _endpointmarket('list/gainers')
    df = pd.DataFrame(response)
    _correctdate(df)
    return df



def Losers():
    """ Biggest loosers in the market
    """
    response = _endpointmarket('list/losers')
    df = pd.DataFrame(response)
    _correctdate(df)
    return df



def MostActive():
    """ Most actively traded in the market
    """
    response = _endpointmarket('list/mostactive')
    df = pd.DataFrame(response)
    _correctdate(df)
    return df



def InFocus():
    """ In Focus market shares
    """
    response = _endpointmarket('list/infocus')
    df = pd.DataFrame(response)
    _correctdate(df)
    return df



def NewsMarket(last):
    """ Last news on the market. Last must belong between 1 to 50
    """
    if (last < 1) or (last > 50):
        raise ValueError('Wrong value - "last" must be between 1 - 50')
    else:
        response = _endpointmarket('news/last/%s' %last)
        df = pd.DataFrame(response)
        return df


    
def MarketOHLC():
    """ Returns the official open and close for a given symbol$
    
    - Not yet sure if it is the best to show the data 
    """
    response = _endpointmarket('ohlc')
    df = json_normalize(response)
    _correctdate(df)
    return df



def Previous():
    """ Returns previous day adjusted price data for the whole market
    """
    
    response = _endpointmarket('previous')
    data = []
    for i in response.keys():
        data.append(response[i])

    df = pd.DataFrame(data)
    _correctdate(df)
    return df



def SectorPerformance():
    """ Returns previous sector performance
    """

    response = _endpointmarket('sector-performance')
    df = json_normalize(response)
    _correctdate(df)
    return df.drop(['type'], axis=1)







    
