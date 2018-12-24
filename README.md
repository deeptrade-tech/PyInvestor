# PyInvestor

PyInvestor is a python wrapper for the IEX API.


[![](https://travis-ci.com/SamurAi-sarl/PyInvestor.svg?token=1ybw2N4PGqXLfqpxx5kG&branch=master)]()
[![](https://img.shields.io/github/license/SamurAi-sarl/PyInvestor.svg)](https://github.com/SamurAi-sarl/PyInvestor)
![Python 3.6](https://img.shields.io/badge/Python-3.6-blue.svg)

## Features

As of now, *PyInvestor* is a wrapper for the IEX API. However, 
we have the ambition to grow it and integrate several financial
APIs into one single Python library, *PyInvestor*.

  
## Dependencies

- Pandas
- Requests

## Installation

``` bash
pip install pyinvestor
```

## Example

### Market

__SectorPerformance__

``` python
from PyInvestor import market
market.SectorPerformance()
```
![text]('/docs/market.gif')


### Stock

__Earnings__

```python
from PyInvestor.stock import Stock
Stock.Earnings()
```


## Todos



