# -*- coding: utf-8 -*-
"""
Created on Sun Oct 01 17:27:34 2017

@author: Administrator
"""

'''matplotlib.pyplot.axis(*v,**kwargs)获得或设置轴性质的简便方法
不带参数调用：
    ♍ axis(),返回当前的轴范围[xmin,xmax,ymin,ymax]
    ♍ axis(v),设置x和y轴的最大最小值，v=[xmin,xmax,ymin,ymax]
    ♍ axis(off),关掉轴线和标签
    ♍ axis('equal'),改变x或y的范围，使得x和y的相同增量有相同长度
    ♍ axis('scaled'),通过改变plot box的维数而不是axis的数据范围来达到同样的效果。
    ♍ axis('tight'),改变x和y轴的范围，使得所有数据展现。
    ♍ axis('image'),scaled（缩放）的轴范围与数据范围相等吗
    ♍ axis('square'),改变x轴和y轴的范围(xmax - xmin)和(ymax - ymin)，并具有相同的缩放比例，从而形成一个正方形的图形
'''

'''matplotlib.pyplot.xlim(*args,**kwargs)获取或设置当前x轴的范围
  xmin,xmax=xlim():返回当前的x范围
  xlim((xmin,xmax)):设置xlim为xmin,xmax
  xlim(xmin,xmax):设置xlim为xmin,xmax
如果你不指定args，你可以将xmin和xmax作为kwargs传递，例如：
  xlim(xmax=3):min不变，调整max
  xlim(xmin=1):max不变，调整min