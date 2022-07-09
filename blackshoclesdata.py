import pandas as py
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import pandas_datareader.data as web
import datetime as dt
from datetime import datetime, date
from black_scholes import *

"""
Data Collections
"""

stock = 'SPY'
expiry = '12-18-2023'
strike_price =  370
today = datetime.today()
one_year_ago = today.replace(year = today.year - 1)

# df = web.DataReader('GE', 'yahoo', start='2019-09-10', end='2019-10-09')
df = web.DataReader(stock, 'yahoo', one_year_ago, today)

df = df.sort_values(by='Date')
df = df.dropna()
df = df.assign(close_day_before = df['Close'].shift(1))


df['returns'] = ((df.Close - df.close_day_before)/df.close_day_before)

# 252 number of days market open

sigma = np.sqrt(252) * df['returns'].std()
uty = (web.DataReader(  "^TNX", 'yahoo', today.replace(day=today.day-1), today)['Close'].iloc[-1])/100  # Treasury yield 10 yr
lcp = df['Close'].iloc[-1]  #last cost price
t = (datetime.strptime(expiry, "%m-%d-%Y") - datetime.utcnow()).days / 365

print('The Option Price is: ', bs_call(lcp, strike_price, t, uty, sigma))  # S,K,T,R,Sigma


