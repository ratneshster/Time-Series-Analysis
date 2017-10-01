# Cryptocurrency Time-Series Analysis

[Blockchain](https://en.wikipedia.org/wiki/Blockchain) and [cryptocurrencies](https://en.wikipedia.org/wiki/Cryptocurrency) are a hot topic lately. Since the whole thing about Blockchain and cryptocurrencies such as [Bitcoin](https://bitcoin.org/en/), [Ethereum](https://ethereum.org/) and [Litecoin](https://litecoin.org/) has also drawn my attention, i thought it's time to make a short tutorials about analysing crypto currencies using Time-Series methods.

The data itself comes from [Quandl](https://www.quandl.com/). This tutorial is using free available such as the data of the [GDAX (Global Digital Asset Exchange)](https://www.quandl.com/data/GDAX-GDAX-Global-Digital-Asset-Exchange), the world’s most popular place to buy and sell bitcoin. If you want to build something close to real-time, you might look for other data sources because GDAX updates only once per day. However, for understanding Time-Series analysis, GDAXs data are sufficient.<br><br><br>

## 1. Cryptocurrency Time-Series Tutorials

#### 001 Compare and Display
Retrieve, compare and display Time-Series data of cryptocurrencies. This tutorial will show you a few basics how to handle Time-Series data using Pandas DataFrame.

#### 002 Seasonal Decomposition
Calculate Seasonal Decomposition for cryptocurrency Time-Series using moving averages. Please note, this is a naive decomposition. More sophisticated methods should be preferred. In this example the additive model (Y[t] = T[t] + S[t] + e[t]) was applied.

#### 003 Autocorrelation
Compare autocorrelated Time-Series data of Bitcoin, Litecoin and Ethereum.

#### 004 Trends and Cycles
Applying ARIMA (Autoregressive Integrated Moving Average) and stochastic cycle model to demonstrate the difference of trend from cycle on cryptocurrency data.<br><br><br>

## 2. Flask Webservice for Data Visualization
The second part of this tutorial is to create [Flask webservice](http://flask.pocoo.org/) to visualize our data in the web browser. Please note, this is an ongoing process and is not ready by now (**09/30/2017**)
