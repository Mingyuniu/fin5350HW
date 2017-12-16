import numpy as np
from scipy.stats import binom





class VanillaOption(object):	
    def __init__(self,strike,expiry):       
        self.strike = strike
        self.expiry = expiry
    def payoff(self, spot):
        pass

class VanillaCallOption(VanillaOption):	
    def payoff(self, spot):
        return np.maximum(spot - self.strike, 0.0)
class VanillaPutOption(VanillaOption):
    def payoff(self, spot):
        return np.maximum(self.strike - spot, 0.0)
    


def AmericanBinomialPricer(option, spot, rate, vol, div, steps):
    numberNodes = steps + 1
    dt = T/ steps
    u = np.exp(((rate - div) * dt) + vol * np.sqrt(dt)) 
    d = np.exp(((rate - div) * dt) - vol * np.sqrt(dt))
    pu = (np.exp(rate*dt)-d)/(u-d)
    pd = 1 - pu
    
    discount = np.exp(-rate * dt)
    dpu = discount * pu
    dpd = discount * pd
    spotT = np.zeros(numberNodes)
    callT = np.zeros(numberNodes)
    
    for i in range(numberNodes):
        spotT[i] = spot * (u ** (steps - i)) * (d ** i)
        callT[i] += option.value (spotT[i])

    for i in range((steps-1), -1, -1):
        for j in range(i+1):
            callT[j] = dpu * callT[j] + dpd * callT[j+1]
            spotT[j] = spotT[j]/u
            callT[j] = np.maximum(callT[j], option.value(spotT[j]))
            
    return callT[0]




def NaiveMonteCarloPricer(option, spot, rate, vol, div, nreps):
    Z=np.random.normal(size=nreps)
    disc=np.exp(-rate*T)
    
    S_T=spot*np.exp((rate-div-0.5*vol**2)*T+vol*np.sqrt(T)*Z)
    payoff_T=option.payoff(S_T)
    meanprice=payoff_T.mean()*disc
    return meanprice
   
spot = 41.0
strike = 40.0
rate = 0.08
T = 1.0
vol = 0.30
div = 0.0
steps = 3

theCall = VanillaCallOption(strike,T)
EuropeanCallMontecarlo=NaiveMonteCarloPricer(theCall,spot,rate,vol,div,100000)
thePut = VanillaPutOption(strike, T)
EuropeanPutMontecarlo=NaiveMonteCarloPricer(thePut,spot,rate,vol,div,100000)
   
  
    
    
print("the monte carlo call option price is",EuropeanCallMontecarlo)
print("the monte carlo put option price is",EuropeanPutMontecarlo)
    