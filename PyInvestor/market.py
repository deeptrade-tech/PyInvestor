from utils import IEX_URL, _endpointmarket, _correctdate
import requests
import pandas as pd



        
        
def Crypto():
    """ returns an array of quotes for all cryptocurrencies supported by the IEX API. 
    """
    response = _endpointmarket('crypto')
    df = pd.DataFrame(response)
    _correctdate(df)
    return df

    
def IPO():
    """ list of upcoming or today IPOs scheduled for the current
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


def NewsMarket(last):
    """ Last news on the market. Last must belong between 1 to 50
    """
    if (last < 1) or (last > 50):
        raise ValueError('Wrong value - "last" must be between 1 - 50')



    
    
