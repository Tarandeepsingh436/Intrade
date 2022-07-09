from gettext import npgettext
from math import log,sqrt,pi,exp
from scipy.stats import norm
from pandas import Series,DataFrame
from datetime import datetime,date

"""
C = call option price
N = CDF of the normal distribution
St = spot price of an asset
K = strike price
r = risk-free interest rate
t = time to maturity
o- = volatility of the asset
"""

# Probability of Receiving the Stock at the Expiration of the Option
def d1(S,K,T,r,sigma):
    d1 = (log(S/K)+(r+sigma**2/2)*T)/(sigma*sqrt(T))
    return d1

# Risk-adjusted Probability
def d2(S,K,T,r,sigma):
    return d1(S,K,T,r,sigma)-sigma*sqrt(T)

# Call Options Price
def bs_call(S,K,T,r,sigma):
    return S*norm.cdf(d1(S,K,T,r,sigma))-K*exp(-r*T)*norm.cdf(d2(S,K,T,r,sigma))

# Put Options Price
def bs_put(S,K,T,r,sigma):
    return K*exp(-r*T)*norm.cdf(-d2(S,K,T,r,sigma))-S*norm.cdf(-d1(S,K,T,r,sigma))



































