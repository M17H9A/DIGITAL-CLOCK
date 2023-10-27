import os
import time
import pandas_datareader_as web
from winotify import Notification, audio

tickers = ["AAPL", "FB", "NVDA", "GS", "WFC"]

for ticker in tickers:
    print(web.DataReader(ticker,"yahoo").iloc[-1]['Close'])

#upper_limits = [200, 400, 500, 300, 100]
#lower_limits = [200, 400, 500, 300, 100]

