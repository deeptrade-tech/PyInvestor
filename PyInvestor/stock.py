from PyInvestor.utils import IEX_URL, timerange_split, timerange_chart , _endpoint, _correctdate
import requests
import pandas as pd
import collections

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
        

    def Company(self):
        """ returns information related to the company
        """
        response = _endpoint(self.key, self.symbol, 'company')
        df = pd.DataFrame(response)
        df = df.drop(['tags'], axis=1)
        return df.drop_duplicates()

    

    def Deep(self):
        """ Deep is used to receive real-time depth of book quotations directly from IEX.
        """
        request_url = "https://api.iextrading.com/1.0/deep?symbols=%s" %self.symbol
        response = requests.get(request_url)
        response_json = response.json()
        try:
            dic = {
                'volume': response_json['volume'],
                'latestUpdate': response_json['lastUpdated'],
                'bids': response_json['bids'][0]['price'],
                'sizebids': response_json['bids'][0]['size'],
                'asks': response_json['asks'][0]['price'],
                'sizeasks': response_json['asks'][0]['size']
                 }
        except:
            dic = {
                'volume': response_json['volume'],
                'latestUpdate': response_json['lastUpdated']
            }
        df = pd.DataFrame(dic, index=[0])
        _correctdate(df)
        return df
        
    

    def DelayedQuote(self):
        """ returns the 15 minute delayed market quote 
        """
        response = _endpoint(self.key, self.symbol, 'delayed-quote')
        df = pd.Series(response).to_frame().T
        _correctdate(df)
        return df

    
    def Dividends(self, timerange):
        """ returns the historical dividends based on the historical market data
        """
        if timerange not in timerange_split:
            raise ValueError('%s not a valid value. Please select: "5y","2y","1y","ytd","6m","3m","1m"')
        else:
            response = _endpoint(self.key, self.symbol, 'dividends/%s' %timerange)
        return pd.DataFrame(response)
        

    def Earnings(self):
        """ returns data from the four most recent reported quarters
        """
        response = _endpoint(self.key, self.symbol, 'earnings')
        return pd.DataFrame(response['earnings'])

    
    def EffectiveSpread(self):
        """ returns an array of effective spread, eligible volume, and price 
            improvement of a stock, by market. Effective spread is designed to 
            measure marketable orders executable in relation to the market 
            center's quoted spread and takes into account hidden and midpoint
            liquidity available at each market center.
        """
        response =  _endpoint(self.key, self.symbol, 'effective-spread')
        return pd.DataFrame(response)

    
    def Financials(self):
        """ returns income statement, balance sheet, and cash flow data from the four
            most recent reported quarters.
        """
        response = _endpoint(self.key, self.symbol, 'financials')
        return pd.DataFrame(response['financials'])


    def Stats(self):
        """ returns certain important number in relation with a stock
        """
        response = _endpoint(self.key, self.symbol, 'stats')
        return pd.Series(response).to_frame().T

    
    def LargestTrades(self):
        """ returns 15 minute delayed, last sale eligible trades
        """ 
        response = _endpoint(self.key, self.symbol, 'largest-trades')
        df = pd.DataFrame(response)
        _correctdate(df)
        return df


    def News(self, lastndays=10):
        if (lastndays > 50) or (lastndays < 1):
            raise ValueError('Value of last is not correct. It must in between [1,50]')
        else:
            response = _endpoint(self.key, self.symbol, 'news/last/%s' %lastndays)
            df = pd.DataFrame(response)
        return df
    
        
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
        dic[self.symbol]['close_time'] = response['close']['time']
        dic[self.symbol]['open_time'] = response['open']['time']
        df = pd.DataFrame(dic)
        _correctdate(df)
        return df

    
    def Previous(self):
        """ returns previous day adjusted price data for a single stock
        """
        response = _endpoint(self.key, self.symbol, 'previous')
        return pd.DataFrame(response, index=[response['symbol']])


    def Price(self):
        """ returns a single number, corresponding to the IEX real time price, the 15 minute delayed market price, 
        or the previous close price 
        """
        return _endpoint(self.key, self.symbol, 'price')


    def Quote(self, displayPercent=False):
        """ returns several quoting prices such as calculationPrice, latestPrice, delayedPrice
        Option: displayPercent -- all percentage values will be multiplied by a factor 100
        """
        if displayPercent == False:
            response = _endpoint(self.key, self.symbol, 'quote')
        else:
            response = _endpoint(self.key, self.symbol, 'quote?displayPercent=true')
        df = pd.Series(response).to_frame().T
        _correctdate(df)
        return df

    
    def Relevant(self):
        """ similar to peers endpoint, except this will return most active market symbols when peers
        are not available.
        """
        response = _endpoint(self.key, self.symbol, 'relevant')
        return response['symbols']


    def Splits(self, timerange):
        """ returns the different splits that occured for a particular range of dates "timerange"
        """
        if timerange not in timerange_split:
            raise ValueError('%s not  a valid value, please enter: "5y", "2y", "1y", "ytd", "6m", "3m", "1m"' %timerange)
        else:
            response = _endpoint(self.key, self.symbol, 'splits/%s' %timerange)
        return pd.DataFrame(response)


    def Tags(self):
        response = _endpoint(self.key, self.symbol, 'company')
        return response['tags']

    
    def TimeSeries(self, timerange='1m'):
        """ returns the historically adjusted market-wide data based on the timerange.
            this turns out to be the same as the chart endpoint of IEX API.
        """
        if timerange not in timerange_chart:
            raise ValueError('%s not a valid value, please enter: "5y", "2y", "1y", "ytd", "6m", "3m", "1m", "1d", "date", "dynamic"' %timerange)
        else:
            response = _endpoint(self.key, self.symbol, 'time-series/%s' %timerange) # still to check if kwargs work
        return pd.DataFrame(response)
            

    def VolumebyVenue(self):
        """ returns 15 minute delayed and 30 day average consolidated volume
            percentage of a stock, by market. This call will always return 13 values, and will be 
            sorted in ascending order by current day trading volume percentage
        """
        response =  _endpoint(self.key, self.symbol, 'volume-by-venue')
        return pd.DataFrame(response)
    
        
    

