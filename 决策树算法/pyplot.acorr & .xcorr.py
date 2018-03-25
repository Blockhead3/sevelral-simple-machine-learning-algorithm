# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 17:19:20 2017

@author: Administrator
"""

''' matplotlib.pyplot.acorr(x,hold=None,data=None,**kwargs):绘制x的自相关（Plot the autocorrelation of x.自相关，也称为序列相关，是一个信号与一个延迟副本本身作为一个延迟的函数的相关性）'''
# x--标量序列;hold--布尔型，可选参数，默认true，弃用;
# usevlines--布尔，可选参数，默认Ture(如果Ture，Axes.vline(子图的数轴（垂直线）)从原点开始画垂直线，否则，用Axes.plot)
# maxlags--整数，可选参数，默认值10，显示的滞后数，若值为None，返回所有2*len(x)-1个滞后时间
#normed--布尔型，可选参数，默认值:True(如果True，输入向量被标准化到单位长度)


'''matplotlib.pyplot.xcorr(x,y,normed=True,detrend=<function detrend_none>,\
usevlines=True,maxlags=10,hold=None,data=None,**kwargs) #绘制x与y的互相关'''
# x--长度为n的标量序列；y--x--长度为n的标量序列；hold--布尔型，可选参数，默认true，弃用。
# detrend--可调用的，可选的，默认值:mlab.detrend_none，默认没有规范化
# normed--布尔，可选，默认值：True(输入向量被标准化到单位长度)
# usevlines--（同上） ；maxlags--（同上）

#例2(pyplot.acorr与pyplot.xcorr)上图是xcorr,下图是acorr
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)#seed()函数，给随机对象一个种子值，用于产生随机序列
x,y=np.random.randn(2,100)#numpy.random.randn():从标准正态分布中返回一个或多个样本值，2行100列
fig=plt.figure()#调用figure()创建figure(图表)对象,即画布。
ax1=fig.add_subplot(211)#在整张图上加入一个子图，211的意思是在一个2行1列的子图中的第1张
ax1.xcorr(x,y,usevlines=True,maxlags=50,normed=True,lw=2)
ax1.grid(True)
ax1.axhline(0,color='black',lw=2)#在y=0处画一条黑色横线，横跨X的取值范围

ax2=fig.add_subplot(212,sharex=ax1)
ax2.acorr(x,usevlines=True,maxlags=50,normed=True,lw=2)
ax2.grid(True)
ax2.axhline(0,color='black',lw=2)#在y=0处画一条黑色横线，横跨X的取值范围

plt.show(ax2)