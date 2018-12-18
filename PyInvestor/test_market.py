import unittest
from PyInvestor.market import *

class MarketTest(unittest.TestCase):


    def test_crypto(self):
        Crypto()

    
    def test_upcomingipo(self):
        UpcomingIPO()

    
    def test_todayipo(self):
        TodayIPO()

    
    def test_gainers(self):
        Gainers()

    
    def test_losers(self):
        Losers()


    def test_mostactive(self):
        MostActive()


    def test_infocus(self):
        InFocus()


    def test_newsmarket(self):
        NewsMarket(last=50)


    def test_marketohlc(self):
        MarketOHLC()


    def test_previous(self):
        Previous()


    def test_sectorperformance(self):
        SectorPerformance()

    


if __name__ == '__main__':
    unittest.main()
