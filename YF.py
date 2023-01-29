
import yfinance as yf


tsla = yf.Ticker('tsla')

tslaInfo = tsla.info

for key,value in tslaInfo.items():
    print(key, ':', value)
    
    
    