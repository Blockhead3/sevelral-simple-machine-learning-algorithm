# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 09:35:17 2017

@author: Cabbge
轨道：trace
"""

'''
 NumPy array (pymc3.backends.NDArray) 
 Text files (pymc3.backends.Text) 
 SQLite (pymc3.backends.SQLite 



db=pm.backends.Text('test')
trace=pm.sample(2000,trace=db)#采样结果保存到csv文件
trace['x']#为终端选择一个变量x，用变量或变量名的索引访问后端
#teace.x
trace['x',1000:]#丢弃每个链的前N个值
trace.get_values('x',burn=1000,combine=False)#丢弃前1000个迭代，保持每个链是分离数组
trace.get_values('x',burn=1000,chains=[0,2])#chains:用于限制取回的链
sliced_trace=trace[1000:]#支持切片，

trace=pm.backends.text.load('test')#加载一个保存的后端

调用后端（backends）采样的三种方法

setup(draws number,chain number)
record方法，保存抽样结果，用一个值的字典映射变量名
close:完成和清空后端


backends.base.BaseTrace:基本的存储类别（类型）,提供了所有的PyMCh后端使用的通常模型设置

几种选择方法：
get_values:从后端中选择变量
_slice:定义后端如何返回一份自己，如果后端被索引为一个分片范围，调用它
point:在一次迭代中为每个变量返回值，如果后端用一个整数索引，用它
__len__:返回抽样数目
'''
import pymc3 as pm

from pm.backends.ndarray import NDArray
from pm.backends.text import Text
from pm.backends.sqlite import SQLite
from pm.backends.hdf5 import HDF5

_shortcuts={'text':{'backend':Text,'name':'mcmc'},
            'sqlite':{'backend':SQLite,'name':'mcmc.sqlite'},
            'hdf5':{'backend':HDF5,'name':'mcmc.hdf5'}}
            
