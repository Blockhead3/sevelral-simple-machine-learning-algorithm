# -*- coding: utf-8 -*-
"""
Created on Fri Oct 06 18:23:46 2017

@author: cabbage
"""

'''matplotlib.pyplot.errorbar()绘制误差棒
在yerr和xerr中绘制x和y的错误增量
参数：
    x:scalar or array like
    y:scalar or array like
    xerr/yerr:scalar or array like,可选，若是标量、len(N)数组类对象或一个N元数组类对象，误差棒绘制在相对于数据的+/-value处
              若是2×N的序列，误差棒画在相对于数据在-row1 and +row2处
    fmt:格式字符串， 绘制的格式符号
    ecolor:mpl color,  误差棒颜色
    elinewidth:错误棒的线宽。如果没有，使用linewidth       
    capsize:点处误差棒帽的宽度
    capthick:控制误差棒帽的厚度
    barsabove:若True,将errorbars绘制在plot符号上方。默认的是下面
    lolims/uplims/xlolims/xuplims:这些参数可以用来表示一个值只提供上限/下限
    errorevery:例如，errorevery=5，每5个数据点的errorbars将被绘制
'''

#例（演示errorbar函数）
import numpy as np
import matplotlib.pyplot as plt

x=np.arange(0.1,4,0.5)
y=np.exp(-x)

fig,ax=plt.subplots()
ax.errorbar(x,y,xerr=0.2,yerr=0.4)
plt.show()  