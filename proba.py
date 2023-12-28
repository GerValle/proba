#%% 

import yfinance as yf


symbols = ["AAPL", "TWTR", "MSFT"]


Tickers = yf.Tickers(symbols)

history = Tickers.history('500d')['Close']

returns = history.pct_change()

returns.plot()

