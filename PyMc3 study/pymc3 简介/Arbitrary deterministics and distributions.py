# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 18:17:00 2017

@author: Cabbage
"""
import numpy as np
import pymc3 as pm
import theano.tensor as tt
from theano.compile.ops import as_op

@as_op(itypes=[tt.lscalar],otypes=[tt.lscalar])
def crazy_modulo3(value):
    if value>0:
        return value%3
    else:
        return (-value+1)%3
        
'''
with pm.Model() as model_deteministic:
    a=pm.Poisson('a',1)
    b=crazy_modulo3(a)
'''

with pm.Model() as model:
    alpha=pm.Uniform('intercept',-100,100)
    beta=pm.DensityDist('beta',lambda value:-1.5*tt.log(1+value**2),testval=0)
    eps=pm.DensityDist('eps',lambda value:-tt.log(tt.abs_(value)),testval=1)
    
    like=pm.Normal('y_est',mu=alpha+beta*x,sd=eps,observed=y)
    
    
class Beta(pm.Continuous):
    def __init__(self,mu,*args,**Kwargs):
        super(Beta,self).__init__(*args,**Kwargs)
        self.mu=mu
        self.mode=mu
        
    def logp(self,value):
        mu=self.mu
        return beta_logp(value-mu)
        
def beta_logp(value):
    return -1.5*np.log(1+(value)**2)
    
    
with pm.Model() as model:
    beta=Beta('slope',mu=0,testval=0)
    
        

