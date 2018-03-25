# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 17:19:11 2017

@author: Cabbage
"""

import numpy as np
import pymc3 as pm
from scipy import optimize
import matplotlib.pyplot as plt

disaster_data=np.ma.masked_values([4, 5, 4, 0, 1, 4, 3, 4, 0, 6, 3, 3, 4, 0, 2, 6,
                            3, 3, 5, 4, 5, 3, 1, 4, 4, 1, 5, 5, 3, 4, 2, 5,
                            2, 2, 3, 4, 2, 1, 3, -999, 2, 1, 1, 1, 1, 3, 0, 0,
                            1, 0, 1, 1, 0, 0, 3, 1, 0, 3, 2, 2, 0, 1, 1, 1,
                            0, 1, 0, 1, 0, 0, 0, 2, 1, 0, 0, 0, 1, 1, 0, 2,
                            3, 3, 1, -999, 2, 1, 1, 1, 1, 2, 4, 2, 0, 0, 1, 4,
                            0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1],value=-999)
year=np.arange(1851,1962)

plt.plot(year,disaster_data,'o',markersize=8)
plt.ylabel("Disaster count")
plt.xlabel("year")


with pm.Model() as disaster_model:
    
    switchpoint=pm.DiscreteUniform('switchpoint',lower=year.min(),upper=year.max(),testval=1900)
    early_rate=pm.Exponential('early_rate',1)
    late_rate=pm.Exponential('late_rate',1)
    rate=pm.math.switch(switchpoint>=year,early_rate,late_rate)
    disasters=pm.Poisson('disaters',rate,observed=disaster_data)
    
    
    
with disaster_model:
    trace=pm.sample(10000)
    
pm.traceplot(trace)
