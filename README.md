# PyInvestor

PyInvestor is a python wrapper for the IEX API.


[![](https://travis-ci.com/SamurAi-sarl/PyInvestor.svg?token=1ybw2N4PGqXLfqpxx5kG&branch=master)]()
[![](https://img.shields.io/github/license/SamurAi-sarl/PyInvestor.svg)](https://github.com/SamurAi-sarl/PyInvestor)
![Python 3.6](https://img.shields.io/badge/Python-3.6-blue.svg)
[![Documentation Status](https://readthedocs.org/projects/ansicolortags/badge/?version=latest)](https://samurai-sarl.github.io/PyInvestor/)


[Read the docs](https://samurai-sarl.github.io/PyInvestor/) for details related to the different methods in **PyInvestor**.


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



## Legal

As **PyInvestor** is a wrapper for the IEX API, we must provide:

> Data provided  for free by [IEX](https://iextrading.com/developer/). 
> View [IEX's Terms of Use](https://iextrading.com/api-exhibit-a/)

