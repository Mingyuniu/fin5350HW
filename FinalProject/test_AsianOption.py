# -*- coding: utf-8 -*-
# Mingyu Niu(A02023845)  Nan Guo(A01755223)

from AsianOption.data import MarketData
from AsianOption.payoff import VanillaPayoff, call_payoff
from AsianOption.engine import MonteCarloEngine, ArithmeticPricer, GeometricPricer
from AsianOption.facade import OptionFacade




spot=100.0
rate=0.06
volatility = 0.20
dividend = 0.03
thedata = MarketData( spot,rate, volatility, dividend)


expiry = 1.0
strike = 100
thecall = VanillaPayoff(expiry, strike, call_payoff)


replications=100
time_steps = 10
pricer =ArithmeticPricer
mcengine = MonteCarloEngine(replications, time_steps, pricer)

## Calculate the price
option1 = OptionFacade(thecall, mcengine, thedata)
price1 = option1.price()
print("The call price  is", price1)





# -*- coding: utf-8 -*-

