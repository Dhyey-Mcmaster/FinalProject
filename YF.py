# TSLA, SPY, APPLE, META, GOOGLE

import yfinance as yf

TSLA = yf.Ticker('TSLA')

TSLAInfo = TSLA.fast_info

for key,value in TSLAInfo.items():
    print(key, ':', value)
    
tickers = ['tsla']
for ticker in tickers:
    ticker_yahoo = yf.Ticker(ticker)
    data = ticker_yahoo.history()
    last_quote = data['Close'].iloc[-1]
    print("Telsa", last_quote)
    print(" ")
    print("Open and close")
    print(data)
    

SPY = yf.Ticker('SPY')

SPYInfo = SPY.fast_info

for key,value in SPYInfo.items():
    print(key, ':', value)
    
tickers = ['spy']
for ticker in tickers:
    ticker_yahoo = yf.Ticker(ticker)
    data = ticker_yahoo.history()
    last_quote = data['Close'].iloc[-1]
    print("SPY", last_quote)
    print(" ")
    print("Open and close")
    print(data)
    
    
    
Meta = yf.Ticker('Meta')

MetaInfo = Meta.fast_info

for key,value in MetaInfo.items():
    print(key, ':', value)
    
tickers = ['Meta']
for ticker in tickers:
    ticker_yahoo = yf.Ticker(ticker)
    data = ticker_yahoo.history()
    last_quote = data['Close'].iloc[-1]
    print("Meta", last_quote)
    print(" ")
    print("Open and close")
    print(data)
    

AAPL = yf.Ticker('AAPL')

AAPLInfo = AAPL.fast_info

for key,value in AAPLInfo.items():
    print(key, ':', value)
    
tickers = ['AAPL']
for ticker in tickers:
    ticker_yahoo = yf.Ticker(ticker)
    data = ticker_yahoo.history()
    last_quote = data['Close'].iloc[-1]
    print("Apple", last_quote)
    print(" ")
    print("Open and close")
    print(data)
    
GOOGL = yf.Ticker('GOOGL')

GOOGLInfo = GOOGL.fast_info

for key,value in SPYInfo.items():
    print(key, ':', value)
    
tickers = ['GOOGL']
for ticker in tickers:
    ticker_yahoo = yf.Ticker(ticker)
    data = ticker_yahoo.history()
    last_quote = data['Close'].iloc[-1]
    print("GOOGLE", last_quote)
    print(" ")
    print("Open and close")
    print(data)
