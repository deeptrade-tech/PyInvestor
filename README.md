# PyInvestor

PyInvestor is a python wrapper for the IEX API.


[![](https://travis-ci.com/SamurAi-sarl/PyInvestor.svg?token=1ybw2N4PGqXLfqpxx5kG&branch=master)]()
[![](https://img.shields.io/github/license/SamurAi-sarl/PyInvestor.svg)](https://github.com/SamurAi-sarl/PyInvestor)
![Python 3.6](https://img.shields.io/badge/Python-3.6-blue.svg)
[![Documentation Status](https://readthedocs.org/projects/ansicolortags/badge/?version=latest)](https://samurai-sarl.github.io/PyInvestor/)

## Documentation

The documentation related to the details of the different methods of **PyInvestor** is found here:
[https://samurai-sarl.github.io/PyInvestor/](https://samurai-sarl.github.io/PyInvestor/) 


## Features

As of now, **PyInvestor** is a wrapper for the IEX API. However, 
we have the ambition to grow it and integrate several financial
APIs into one single Python library, **PyInvestor**.

 - IEX Stocks app using the stocks endpoint;
 - Access to the OHLC of more than 7k stocks;
 - Get relevant news at the stock level;
 - Access to fundamental data such as dividends, earnings, etc.

  
## Dependencies

- Pandas
- Requests

## Installation

``` bash
pip install pyinvestor
```

## Examples

### Market

__SectorPerformance__

``` python
from PyInvestor import market
market.SectorPerformance()
```
![text](./docs/market.gif)


### Stock

__Earnings__

```python
from PyInvestor.stock import Stock
AMZN = Stock('AMZN')
AMZN.Earnings()
```
![text](./docs/stock.gif)

## Todos

| API      | Started Integration                       |
|----------|------------------------------------------  |
| IEX      | [![IEX](http://progressed.io/bar/75)]()   |
| Quandl   | [![Quandl](http://progressed.io/bar/0)]() |
| News API | [![Quandl](http://progressed.io/bar/0)]() |



## Legal

As **PyInvestor** is a wrapper for the IEX API, we have to say that

> Data is provided  for free by [IEX](https://iextrading.com/developer/). 
> View [IEX's Terms of Use](https://iextrading.com/api-exhibit-a/)

