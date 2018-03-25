# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 17:24:58 2017

@author: Cabbage
随机数种子
numpy.random.seed()的使用
seed( ) 用于指定随机数生成时所用算法开始的整数值，
如果使用相同的seed( )值，则每次生成的随即数都相同，
如果不设置这个值，则系统根据时间来自己选择这个值，
此时每次生成的随机数因时间差异而不同
设置的seed()值仅一次有效
"""

import numpy as np

num=0
while num<5:
    np.random.seed(5)
    print np.random.random()
    num+=1
#运行结果完全相同    
    
num=0
np.random.seed(5)
while num<5:
    print np.random.random()
    num+=1
#运行结果不同
    