# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 18:38:21 2017

@author: Cabbage
"""
import numpy as np
import pymc3 as pm

import pandas

df=pandas.DataFrame({'x1':X1,'x2':X2,'y':Y})

from pymc3.glm import CLM

with pm.Model() as model_glm:
    GLM.from_formula('y~x1+x2',df)
    trace=pm.sample()


from pymc3.glm.families import Binomial

df_logistic = pandas.DataFrame({'x1': X1, 'y': Y > np.median(Y)})

with pm.Model() as model_glm_logistic:
    GLM.from_formula('y ~ x1', df_logistic, family=Binomial())    