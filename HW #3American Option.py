#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 05 21:57:25 2017

@author: Mingyu NIu
"""

import numpy as np

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

def AmericanBinomialPricer(payoff, spot, rate, volatility, dividend, steps):
    numberNodes = steps + 1
    dt = T/ steps
    u = np.exp(((rate - dividend) * dt) + volatility * np.sqrt(dt)) 
    d = np.exp(((rate - dividend) * dt) - volatility * np.sqrt(dt))
    pu = (np.exp(rate*dt)-d)/(u-d)
    pd = 1 - pu
    
    discount = np.exp(-rate * dt)
    dpu = discount * pu
    dpd = discount * pd
    spotT = np.zeros(numberNodes)
    callT = np.zeros(numberNodes)
    
    for i in range(numberNodes):
        spotT[i] = spot * (u ** (steps - i)) * (d ** i)
        callT[i] += payoff.value(spotT[i])

    for i in range((steps-1), -1, -1):
        for j in range(i+1):
            callT[j] = dpu * callT[j] + dpd * callT[j+1]
            spotT[j] = spotT[j]/u
            callT[j] = np.maximum(callT[j], payoff.value(spotT[j]))
            
    return callT[0]
        
spot = 41.0
strike = 40.0
rate = 0.08
T = 1.0
volatility = 0.30
dividend = 0.0
steps = 3

theCall = VanillaCallOption(strike,T)
CallPrice = AmericanBinomialPricer(theCall, spot, rate, volatility, dividend, steps)

thePut = VanillaPutOption(strike, expiry)
PutPrice = AmericanBinomialPricer(thePut, spot, rate, volatility, dividend, steps)

print("The price of call option is", CallPrice)
print("The price of put option is", PutPrice)