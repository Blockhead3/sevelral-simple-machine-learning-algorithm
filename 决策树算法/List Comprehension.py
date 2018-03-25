# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 14:27:11 2017

@author: Administrator
"""

#推导式：可以从一个数据序列构建另一个新的数据序列的结构体
#list推导式；字典推导式；集合推导式。
#例1（列表推导式）取3的倍数
a=[i for i in range(30) if i % 3 is 0]
print a
#例2  取3的倍数的平方
def squared(x):
    return x*x
b=[squared(i) for i in range(30) if i %3 is 0]
print b


#例3 过滤长度小于3的字符串，并将剩下的转为大写
names=['Bob','Tom','alice','Jerry','Wendy','Smith']
c=[name.upper() for name in names if len(name)>3]
print c

#例4 求（x,y），其中，x是0--5之间的偶数，y是0--5之间的奇数组成的元组列表
d=[(x,y) for x in range(5) if x % 2 ==0 for y in range(5)if y %2==1]
print d

#例5 求M中3,6，9组成的列表
#import numpy as np
#M=np.array([[1,2,3],[4,5,6],[7,8,9]])
M=[[1,2,3],[4,5,6],[7,8,9]]
print M
e1=[row[2] for row in M]
e2=[M[i][i] for i in range(len(M))]
print e1
print e2


#字典推导
#例1 以字符串及其长度建字典
strings=['import','is','with','if','file','exception']
D={key:val for val ,key in enumerate(strings)}
print D

#集合推导式
#例1 建字符串长度的集合
string1=['a','is','with','if','file','exception']
A={len(s)for s in string1}
print A