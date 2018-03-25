# -*- coding: utf-8 -*-
"""
Created on Thu Nov 09 17:08:36 2017

@author: Cabage
"""

#np.mean()函数:求平均值
#mean(a,axis=None,dtype=None,out=None)
#axis:以居矩阵（m*n）为例，对m*n个数求均值，返回一实数
#axis=0:压缩行，对各列求均值，返回 1*n矩阵
#axis=1:压缩列，对各行求均值，返回 m*1矩阵

import numpy as np
num1=np.array([[1,2,3],[3,4,5],[3,7,1],[9,2,5]])
now2=np.mat(num1)
print now2
print np.mean(now2)
print np.mean(now2,0)
print np.mean(now2,1)