# -*- coding: utf-8 -*-
"""
Created on Fri Nov 03 16:38:04 2017

@author: Administrator
"""

#argsort()函数:返回数组从小到大的索引值
import numpy as np
x=np.array([3,1,2])
print np.argsort(x)

y=np.array([[0,1],[1,0]])
print np.argsort(y,axis=0)#按列排序
print np.argsort(y,axis=1)#按行排序

z=np.array([4,1,3])
print np.argsort(z)#按升序排
print np.argsort(-z)#按降序排列
print z[np.argsort(z)]#通过索引值排序后的数组

a=z[np.argsort(z)]
print a[::-1]