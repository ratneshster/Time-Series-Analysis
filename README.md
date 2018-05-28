# Time-Series Analysis

[Blockchain](https://en.wikipedia.org/wiki/Blockchain) and [cryptocurrencies](https://en.wikipedia.org/wiki/Cryptocurrency) are a hot topic lately. Since the whole thing about Blockchain and cryptocurrencies such as [Bitcoin](https://bitcoin.org/en/), [Ethereum](https://ethereum.org/) and [Litecoin](https://litecoin.org/) has also drawn my attention, i thought it's time to make a short tutorials about analysing crypto currencies using Time-Series methods.


## Note: Technical Indicators (MACD, RSI etc.) coming soon!


## 1. Time-Series Tutorials

#### 001 Compare and Display
Retrieve, compare and display Time-Series data of cryptocurrencies. This tutorial will show you a few basics how to handle Time-Series data using Pandas DataFrame.

#### 002 Pivot Table Visualization
Retrieve, compare, aggregate and visualize Time-Series data of cryptocurrencies using pivot table.

#### 003 Seasonal Decomposition
Calculate Seasonal Decomposition for cryptocurrency Time-Series using moving averages. Please note, this is a naive decomposition. More sophisticated methods should be preferred. In this example the additive model (Y[t] = T[t] + S[t] + e[t]) was applied.

#### 004 Autocorrelation
Compare autocorrelated Time-Series data of Bitcoin, Litecoin and Ethereum.

#### 005 Trends and Cycles
Applying ARIMA (Autoregressive Integrated Moving Average), stochastic cycle model and fourier extrapolation to demonstrate the difference of trend from cycle on cryptocurrency data.

#### 006 Detrending and Dickey Fuller Test
Detrending Time-Series, to remove certain aspects we are assuming to cause the distortion. 
Applying the Augmented Dickey Fuller Test. Time series are stationary if they do not have trend or seasonal effects. 
Summary statistics calculated on the time series are consistent over time, like the mean or the variance of the observations. 
The Augmented Dickey-Fuller test is a type of statistical test called a unit root test. The idea is to figure out how strongly a time series is defined by a trend.<br><br><br>
