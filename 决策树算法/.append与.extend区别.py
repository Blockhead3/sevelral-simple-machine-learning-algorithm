# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 16:11:40 2017

@author: Administrator
"""

a=[1,2,3]
b=[4,5,6]
a.append(b)
print a
a=[1,2,3]
a.extend(b)
print a
print len(a[0])


'''import numpy as np
a=np.array([[1,2,3],
   [6,8,9],
[4,7,0],
[3,5,9]])
print a
print a[0]
print len(a[0])-1'''