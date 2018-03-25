# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 18:28:32 2017

@author: Cabage
"""

import numpy as np

'''a=[1,2,3]
print np.nonzero(a)
#(array([0, 1, 2], dtype=int64),)


b=np.array([[0,0,1],[3,0,0],[0,4,0]])
print b
print np.nonzero(b)
#(array([0, 1, 2], dtype=int64), array([2, 0, 1], dtype=int64))
#b中第0([0,0,1]),1([3,0,0]),2([0,4,0])行元素非0
#第一个非0元素在第2列，第三个非0元素在第0列。。。

c=np.mat([[1,0,0],[0,0,3],[0,2,0],[0,0,5]])
print c
print np.nonzero(c)
#(array([0, 1, 2, 3], dtype=int64), array([0, 2, 1, 2], dtype=int64))
#非0元素分别是第0、1、2、3行，在第0、2、1、2列

print np.nonzero(c)[0]#只返回非0元素所在行
#[0 1 2 3]
'''
e=np.array([[1,2,3,4],[4,5,6,7],[3,4,6,7],[9,0,1,3],[8,2,4,5]])
print e
for i in range(4):
    e1=e[np.nonzero(e[:,i]>6)[0],:]
    print e1

#print e[2,:][0]#第2行第0个元素