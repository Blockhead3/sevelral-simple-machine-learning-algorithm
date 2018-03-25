# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30 21:36:45 2017

@author: Administrator
"""

'''matplotlib.pyplot.axhlines(y=0,xmin=0,xmax=1,hold=None,**kwarg)在图上加一条水平的线
参数：y:(标量，可选，默认0，在水平线的数据坐标轴中y的位置)
     xmin:(标量，可选，默认0,应该在0和1之间，0是图的最左边，图的最右边是1)
     xmax:(标量，可选，默认1,应该在0和1之间，0是图的最左边，1图的最右边。)
     kwargs:kwargs被传递到Line2D，可以用来控制线属性
'''
#例
import matplotlib.pyplot as plt
plt.axhline(linewidth=4,color='r')     
plt.axhline(y=1)
plt.axhline(y=.5,xmin=0.25,xmax=0.75)

''' Line2D性质
agg_fillter----未知
alpha----------float(0.0透明到1.0不透明)
animated-------[True|False]
antialiased 或 aa--[True|False]
axes-----------一个axes实例
clip_box-------一个 matplotlib.transforms.Bbox实例
clip_on-------[True|False]
clip_path-----[ (Path, Transform) | Patch | None ]
color 或 c----绘制的颜色
contains------一个调运函数
dash_capstyle----[‘butt’ | ‘round’ | ‘projecting’]
dash_joinstyle---[‘miter’ | ‘round’ | ‘bevel’]
dashes-----------点上下墨顺序
drawstyle-------[‘default’ | ‘steps’ | ‘steps-pre’ | ‘steps-mid’ | ‘steps-post’]
figure----------一个 matplotlib.figure.Figure实例
fillstyle------[‘full’ | ‘left’ | ‘right’ | ‘bottom’ | ‘top’ | ‘none’]
gid------------一个id字符串
linestyle------[‘solid’ | ‘dashed’, ‘dashdot’, ‘dotted’ | (offset, on-off-dash-seq) | '-' | '--' | '-.' | ':' | 'None' | ' ' | '']
marke----------一个有效地marke风格
markeredgecolor 或 mec----任一绘制颜色
markeredgewidth 或 mew----点的浮动值
markerfacecolor 或 mfc---任一绘制颜色
markerfacecoloralt or mfcalt--任一绘制颜色
markersize or ms-----浮点型
markevery--------[None | int | length-2 tuple of int | slice | list/array of int | float | length-2 tuple of float]
visible---------[True|False]
xdata-----------一维数组
ydata----------一维数组
'''


'''matplotlib.pyplot.axhspan(ymin,ymax,xmin=0,xmax=1,hold=None,**kwargs)添加横跨轴的水平跨距（矩形）
参数：
     ymin:浮点型，在数据单元中水平跨度的下限
     ymax:浮点型，在数据单元中水平跨度的上限
     xmin:浮点型，可选，默认0，轴(相对0 - 1)单位垂直跨度的下限。
     xmax:浮点型，可选，默认1，轴(相对0 - 1)单位垂直跨度的上限。
     edgecolor(ec):mpl颜色规则
     facecolor(fc):mpl颜色规则
     linestyle(ls):[‘solid’ | ‘dashed’, ‘dashdot’, ‘dotted’ | (offset, on-off-dash-seq) | '-' | '--' | '-.' | ':' | 'None' | ' ' | '']
     linewidth(lw):float or None for default
'''
#例
import numpy as np
import matplotlib.pyplot as plt

t=np.arange(-1,2,.01)
s=np.sin(2*np.pi*t)

plt.plot(t,s)
l=plt.axhline(linewidth=8,color='#d62728')#在y=0处画一条粗红横线，它跨越了xrange

l=plt.axhline(y=1)  #在y=1处画一条默认的水平线，横跨xrange

l=plt.axvline(x=1)#在x=1处画一条默认的垂直线，横跨yrange
#在x = 0处画一条粗蓝色的垂直线，它跨越了yrange的上象限
l=plt.axvline(x=0,ymin=0.75,linewidth=8,color='#1f77b4')

#在y =0.5上画一个默认的hline。它跨越了axes中间的一半
l=plt.axhline(y=.5,xmin=0.25,xmax=0.75)

p=plt.axhspan(0.25,0.75,facecolor='0.5',alpha=0.5)

p=plt.axvspan(1.25,1.55,facecolor='#2ca02c',alpha=0.5)

plt.axis([-1,2,-1,2])


plt.show()


