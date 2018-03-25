# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 17:01:09 2017

@author: Administrator
"""

#sum()：内置函数sum(iterable[, start]) ，返回一个数字序列（非字符串）的和，并加上参数'start'的值（默认为0）；如果序列为空，则返回参数start的值（如果start为赋值，则出错）
"""l=range(5)
print l
print(sum(l))
print(sum([2,5,8]))
#.sum()函数是模块numpy的一个函数：sum(a, axis, dtype, out, keepdims),axis=None 将所有元素相加，axis=1:按行相加，axis=0:按列相加。
help(sum)"""

from numpy import *
print(sum([[1,2,3],[4,5,6]],axis=1))#行相加
print(sum([[3,5,6],[2,1,5],[9,8,4]],axis=0))#列相加
