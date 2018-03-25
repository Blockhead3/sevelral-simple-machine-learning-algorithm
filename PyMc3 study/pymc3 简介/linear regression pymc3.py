# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 13:59:30 2017

@author: Administrator
"""

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(123)

alpha,sigma=1,1
beta=[1,2.5]

size=100

x1=np.random.randn(size)
x2=np.random.randn(size)*0.2

y=alpha+beta[0]*x1+beta[1]*x2+np.random.randn(size)*sigma

fig,axes=plt.subplots(1,2,sharex=True,figsize=(10,4))
axes[0].scatter(x1,y)
axes[1].scatter(x2,y)
axes[0].set_ylabel('y')
axes[0].set_xlabel('x1')
axes[1].set_xlabel('x2')


import pymc3 as pm

basic_model=pm.Model()

with basic_model:
    alpha=pm.Normal('alpha',mu=0,sd=10)
    beta=pm.Normal('beta',mu=0,sd=10,shape=2)
    sigma=pm.HalfNormal('sigma',sd=1)
    
    mu=alpha+beta[0]*x1+beta[1]*x2
    
    y_obs=pm.Normal('y_obs',mu=mu,sd=sigma,observed=y)
    
    
map_estimate=pm.find_MAP(model=basic_model)
print map_estimate


from scipy import optimize

map_estimate=pm.find_MAP(model=basic_model,fmin=optimize.fmin_powell)
print map_estimate

'''
with basic_model:
    trace=pm.sample()

print trace['alpha'][-5:]
'''

with basic_model:
    start=pm.find_MAP(fmin=optimize.fmin_powell)
    step=pm.Slice()
    trace=pm.sample(5000,step=step,start=start)
    

_=pm.traceplot(trace)

print pm.summary(trace)