
# Stock methods
These are the different methods that are
already implemented in the library *PyInvestor*
at the stock level.

### `Company`

__Aim__

> Returns information related to the company

__Example__

```python
from PyInvestor.stock import Stock
AMZN = Stock('AMZN')
AMZN.Company()
```

### `DelayedQuote`

__Aim__

> Returns 15 minute delayed market quote

__Example__

```python
from PyInvestor.stock import Stock
AMZN = Stock('AMZN')
AMZN.DelayedQuote()
```

### `Dividends`

__Aim__

> Returns the historical dividends based on 
> on the historical market data

__Example__

```python
from PyInvestor.stock import Stock
AMZN = Stock('AMZN')
AMZN.Dividends()
```

__Option__

 - timerange: value in ["5y", "2y", "1y", "ytd", "6m", "3m", "1m"]


### `Earnings`

__Aim__

> Returns data from the four most  
> recent reported quarters

__Example__

```python
from PyInvestor.stock import Stock
AMZN = Stock('AMZN')
AMZN.Earnings()
```

### `EffectiveSpread`

__Aim__

> Returns an array of effective spread, 
> eligible volume, and prive improvement of
> a stock, by market. Effective spread is 
> designed to measure marketable orders 
> executable in relation to the market center's
> quoted spread and takes into account hidden 
> and midpoint liquidity available at each 
> market center.

__Example__

```python
from PyInvestor.stock import Stock
AMZN = Stock('AMZN')
AMZN.EffectiveSpread()
```

### `Financials`

__Aim__

> Returns income statement, balance sheet, 
> and cash flow data from the four most 
> recent reported quarters.

__Example__

```python
from PyInvestor.stock import Stock
AMZN = Stock('AMZN')
AMZN.Financials()
```

### `Stats`

__Aim__

> Returns certain important numbers in
> relation with a stock.

__Example__

```python
from PyInvestor.stock import Stock
AMZN = Stock('AMZN')
AMZN.Stats()
```

### `LargestTrades`

__Aim__

> Returns 15 min delayed, last sale eligible trades
 

__Example__

```python
from PyInvestor.stock import Stock
AMZN = Stock('AMZN')
AMZN.LargestTrades()
```

### `News`

__Aim__

> Returns stock related news for a certain number
> of last days.
 

__Example__

```python
from PyInvestor.stock import Stock
AMZN = Stock('AMZN')
AMZN.News(lastndays=5)
```

__Options__

- lastndays: value betwen 1 and 50


### `OHLC`

__Aim__

> Returns the official open, high, low and close
> for a given symbol with open and/or close official
> listing time


__Example__

```python
from PyInvestor.stock import Stock
AMZN = Stock('AMZN')
AMZN.OHLC()
```

### `Previous`

__Aim__

> Returns previous day adjusted price data for 
> a single stock


__Example__

```python
from PyInvestor.stock import Stock
AMZN = Stock('AMZN')
AMZN.Previous()
```

### `Price`

__Aim__

> Returns a single number, corresponding to the 
> IEX real time price, the 15 minute delayed market
> price, or the previous close price. 


__Example__

```python
from PyInvestor.stock import Stock
AMZN = Stock('AMZN')
AMZN.Price()
```

### `Quote`

__Aim__

> Returns several quoting prices such as 
> calculationPrice, latestPrice, delayedPrice.


__Example__

```python
from PyInvestor.stock import Stock
AMZN = Stock('AMZN')
AMZN.Quote()
```

__Option__

 - displayPercent: all percentage values will
   be multiplied by a factor 100



### `Relevant`

__Aim__

> This will return the most active market 
> symbols.


__Example__

```python
from PyInvestor.stock import Stock
AMZN = Stock('AMZN')
AMZN.Relevant()
```


### `Splits`

__Aim__

> Returns the different splits that occured
> for a particular range of dates "timerange"


__Example__

```python
from PyInvestor.stock import Stock
AMZN = Stock('AMZN')
AMZN.Splits(timerange = '1m')
```


__Option__

 - timerange: value in ["5y", "2y", "1y", "ytd", "6m", "3m", "1m"]



### `Tags`

__Aim__

> Get the tags related to a particular stock


__Example__

```python
from PyInvestor.stock import Stock
AMZN = Stock('AMZN')
AMZN.Tags()
```


### `TimeSeries`

__Aim__

> Returns the historically adjusted market-wide
> data based on the timerange. 


__Example__

```python
from PyInvestor.stock import Stock
AMZN = Stock('AMZN')
AMZN.TimeSeries()
```

__Option__

 - timerange: value in ["5y", "2y", "1y", "ytd", "6m", "3m", "1m"]



### `VolumebyVenue`

__Aim__

> Returns 15 min delayed and 30 day average consolidation
> volume percentage of a stock, by market. This call will
> always return 13 values, and will be sorted in ascending
> order by current day trading volume percentage. 


__Example__

```python
from PyInvestor.stock import Stock
AMZN = Stock('AMZN')
AMZN.VolumebyVenue()
```















