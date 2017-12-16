import numpy as np
from scipy.stats import binom

class Option:
    def __init__(self, strike, expiry):
        self.strike = strike
        self.expiry = expiry

    def value(self):
        pass

class VanillaCallOption(Option):
    def value(self, spot):
        return np.maximum(spot - self.strike,0.0)

class VanillaPutOption(Option):
    def value(self, spot):
        return np.maximum(self.strike - spot,0.0)

def EuropeanBinomialPricer(option, spot, rate, volatility, dividend, steps):
    numberNodes = steps + 1
    spotT = 0.0
    putT = 0.0
    dt = T/ steps
    u = np.exp(((rate - dividend) * dt) + volatility * np.sqrt(dt)) 
    d = np.exp(((rate - dividend) * dt) - volatility * np.sqrt(dt))
    pu = (np.exp(rate*dt)-d)/(u-d)
    
    for i in range(numberNodes):
        spotT = spot * (u ** (steps - i)) * (d ** (i))
        putT += option.value(spotT) * binom.pmf(steps - i, steps, pu)
    price = putT * np.exp(-rate * T)

    return price
        
spot = 41.0
strike = 40.0
rate = 0.08
T = 1.0
volatility = 0.30
dividend = 0.0
steps = 3

theCall = VanillaCallOption(strike, expiry)
CallPrice = EuropeanBinomialPricer(theCall, spot, rate, volatility, dividend, steps)

thePut = VanillaPutOption(strike, expiry)
PutPrice = EuropeanBinomialPricer(thePut, spot, rate, volatility, dividend, steps)

print("The price of the call option is", CallPrice)
print("The price of the put option is", PutPrice)