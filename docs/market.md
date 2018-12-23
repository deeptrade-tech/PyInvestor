

# Market methods
These are the different methods that are
already implemented in the library *PyInvestor*. 


### `Crypto`

__Aim__

> This will return an array of quotes for all
> Cryptocurrencies supported by the IEX API.


__Example__

``` python
from PyInvestor import market
market.Crypto()
```

### `UpcomingIPO`

__Aim__

> This returns a list of upcoming IPOs scheduled
> for the current and next month. 

__Example__

``` python
from PyInvestor import market
market.UpcomingIPO()
```

### `TodayIPO`

__Aim__

> This returns a list of today's IPOs scheduled 
> for the current and next month.

__Example__

``` python
from PyInvestor import market
market.TodayIPO()
```

### `Gainers`

__Aim__

> List of stocks that got the best performances 
> in percent. 

__Example__

``` python
from PyInvestor import market
market.Gainers()
```

### `Losers`

__Aim__

> List of stocks that got the worst performances
> in percent.

__Example__

``` python
from PyInvestor import market
market.Losers()
```

### `MostActive`

__Aim__

> 
> 

__Example__

``` python
from PyInvestor import market
market.MostActive()
```

### `InFocus`

__Aim__

__Example__

``` python
from PyInvestor import market
market.InFocus()
```


### `NewsMarket`

__Aim__

__Example__

``` python
from PyInvestor import market
market.NewsMarket()
```

### `MarketOHLC`

__Aim__

__Example__

``` python
from PyInvestor import market
market.MarketOHLC()
```

### `Previous`

__Aim__

> Returns previous day 
> an object keyed symbol of price
> data for the whole market. 

__Example__

``` python
from PyInvestor import market
market.Previous()
```

### `SectorPerformance`

__Aim__

> Returns an array of each sector and performance for the
> current trading day. 

__Example__

``` python
from PyInvestor import market
market.SectorPerformance()
```





