import unittest
from PyInvestor.stock import Stock


class StockTest(unittest.TestCase):
    
        
    def test_company(self):
        AMZN = Stock('AMZN')
        AMZN.Company()

    
    def test_delayedquote(self):
        AMZN = Stock('AMZN')
        AMZN.DelayedQuote()

    
    def test_dividends(self):
        AMZN = Stock('AMZN')
        AMZN.Dividends('1y')

    
    def test_earnings(self):
        AMZN = Stock('AMZN')
        AMZN.Earnings()


    def test_effectivespread(self):
        AMZN = Stock('AMZN')
        AMZN.EffectiveSpread()


    def test_financials(self):
        AMZN = Stock('AMZN')
        AMZN.Financials()


    def test_stats(self):
        AMZN = Stock('AMZN')
        AMZN.Stats()


    def test_deep(self):
        AMZN = Stock('AMZN')
        AMZN.Deep()


    def test_largestrades(self):
        AMZN = Stock('AMZN')
        AMZN.LargestTrades()


    def test_news(self):
        AMZN = Stock('AMZN')
        AMZN.News(lastndays = 20)
        AMZN.News()

    def test_ohlc(self):
        AMZN = Stock('AMZN')
        AMZN.OHLC()


    def test_previous(self):
        AMZN = Stock('AMZN')
        AMZN.Previous()


    def test_price(self):
        AMZN = Stock('AMZN')
        AMZN.Price()


    def test_quote(self):
        AMZN = Stock('AMZN')
        AMZN.Quote(displayPercent=True)
        AMZN.Quote()


    def test_relevant(self):
        AMZN = Stock('AMZN')
        AMZN.Relevant()


        
    def test_splits(self):
        AMZN = Stock('AMZN')
        AMZN.Splits('5y')


    def test_tags(self):
        AMZN = Stock('AMZN')
        AMZN.Tags()


    def test_timeseries(self):
        AMZN = Stock('AMZN')
        AMZN.TimeSeries('5y')


    def test_volumebyvenue(self):
        AMZN = Stock('AMZN')
        AMZN.VolumebyVenue()



if __name__ == '__main__':
    unittest.main()
  
