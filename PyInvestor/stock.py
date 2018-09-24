from utils import IEX_URL, _endpoint
import requests
import pandas as pd
import collections
import datetime
"""
TODOs

-  implement a proper way to deal with out of connection requests
"""



class Stock:
    """Gathers data from the IEX endpoints for only one stock
    """

    def __init__(self, symbol):
        """Initialization of the class Stock
        """
        self.symbol = symbol.upper()
        self.key = 'stock'
                    
    
    def Price(self):
        """ returns a single number, corresponding to the IEX real time price, the 15 minute delayed market price, 
        or the previous close price 
        """
        return _endpoint(self.key, self.symbol, 'price')

    
    def OHLC(self): 
        """ returns the official open, high, low and close for a given symbol with open and/or close official listing time 
        """
        response = _endpoint(self.key, self.symbol, 'ohlc')
        dic = collections.defaultdict()
        dic[self.symbol] = {}
        dic[self.symbol]['open'] = response['open']['price']
        dic[self.symbol]['close'] = response['close']['price']
        dic[self.symbol]['high'] = response['high']
        dic[self.symbol]['low'] = response['low']
        dic[self.symbol]['close_time'] = datetime.datetime.fromtimestamp(response['close']['time'] / 1e3)
        dic[self.symbol]['open_time'] = datetime.datetime.fromtimestamp(response['open']['time'] / 1e3)
        df = pd.DataFrame(dic)
        return df

    
    def Peers(self):
        """ returns an array of peers defined by IEX
        """
        return _endpoint(self.key, self.symbol, 'peers')

    
    def Previous(self):
        """ returns previous day adjusted price data for a single stock
        """
        response = _endpoint(self.key, self.symbol, 'previous')
        return pd.DataFrame(response, index=[response['symbol']])


    def Quote(self, displayPercent=False):
        """ returns several quoting prices such as calculationPrice, latestPrice, delayedPrice
        Option: displayPercent -- all percentage values will be multiplied by a factor 100
        """
        response = _endpoint(self.key, self.symbol, 'previous')
        df = pd.DataFrame(response, index=[response['symbol']])
        df = df.drop()


    

    
        
class StockBatch:
    """ Gather data from the IEX endpoints for a list of stocks
    """
    pass
    
    
