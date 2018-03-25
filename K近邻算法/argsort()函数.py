# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 19:33:02 2017

@author: Administrator
"""

# argsort()函数是numpy库中的函数，用于排序。argsort函数返回的是数组值从小到大的索引值
import numpy as np
x=np.array([1,4,3,-1,6,9]) #定义一个一维数组
print(np.argsort(x)) #数组[1,4,3,-1,6,9]从小到大排列分别是[-1,1,3,4,6,9],而它们在数组中的下标（索引值）分别是[3,0,2,1,4,5]，所有输出结果就是数组值从小到大的索引值
print(x[np.argsort(x)])#排序后的数组

x=np.array([[0,3],[2,4]])#定义一个二维数组
print(np.argsort(x,axis=-1))
print(np.argsort(x,axis=0))#按列排序
print(np.argsort(x,axis=1))#按行排序
print(x[np.argsort(x,axis=0)])#？？？
                      

