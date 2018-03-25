# -*- coding: utf-8 -*-
"""
Created on Sun Oct 01 18:32:07 2017

@author: Administrator
"""

#绘制条形图
'''matplotlib.pyplot.bar(left,height,width=0.8,bottom=None,hold=None,data=None,**kwargs)
绘制一个条形图，以下面矩形为边界：left,left+width,bottom,bottom+height 分别是矩形的（left,right,bottom,top边）
参数：
◑left:标量序列，条的左边的x坐标；height:标量序列，条的高。
◐width:标量或数组类，可选，条的宽度，默认0.8；bottom:标量或数组类，可选，条的y坐标，默认：None
◑color:标量或数组类，可选，条面的颜色；edgecolor:标量或数组类，可选，条边界色
◐linewidth:标量或数组类(可选)，条边的宽度，若None,用默认值；若0，不画边。 tick_label:字符串或数组类(可选)，条的刻度标注，默认：None
◑xerr:标量或数组类，可选，若非None,则用来在条形图上生成一个errorbars,默认：None
◐yerr:标量或数组类，可选，若非None,则用来在条形图上生成一个errorbars,默认：None
◐ecolor:标量或数组类，可选,errorbar指定的颜色，默认：None;
◐capsize:标量，可选，在点中，决定errorbar长度； error_kw:字典，可选，
◐orientation:{'vertical','horizontal'},可选，条的方向
◐log:布尔，可选，若True,轴设置为对数尺度
◐kwargs: LineCollection properties.
'''

#例（带有errorbar的堆叠式条形图）

import numpy as np
import matplotlib.pyplot as plt

N=5
menMeans=(20,35,30,35,27)
womenMeans=(25,32,34,20,25)
menStd=(2,3,4,1,2)
womenStd=(3,5,2,3,3)
ind=np.arange(N) #组中x的位置
width=0.35 #条的宽

p1=plt.bar(ind,menMeans,width,color='#d62728',yerr=menStd)
p2=plt.bar(ind,womenMeans,width,bottom=menMeans,yerr=womenStd)

plt.ylabel('Scores')
plt.title('Scores by group and gender')
plt.xticks(ind,('G1','G2','G3','G4','G5'))
plt.yticks(np.arange(0,81,10))
plt.legend((p1[0],p2[0]),('Men','Women'))

plt.show()


'''matplotlib.pyplot.barh(bottom,width,height=0.8,left=None,hold=None,**kwargs)制作横条形图
绘制一个条形图，以下面矩形为边界：left,left+width,bottom,bottom+height 分别是矩形的（left,right,bottom,top边）
参数：
◑left:标量序列，条的左边的x坐标；
◑height:标量序列，条的高，默认 0.8。
◐width:标量或数组类，条的宽度，
◑bottom:标量或数组类，可选，条的y坐标，默认：None
◑color:标量或数组类，可选，条面的颜色；
◑edgecolor:标量或数组类，可选，条边界色
◐linewidth:标量或数组类(可选)，条边的宽度，若None,用默认值；若0，不画边。
◑tick_label:字符串或数组类(可选)，条的刻度标注，默认：None
◑xerr:标量或数组类，可选，若非None,则用来在条形图上生成一个errorbars,默认：None
◐yerr:标量或数组类，可选，若非None,则用来在条形图上生成一个errorbars,默认：None
◐ecolor:标量或数组类，可选,errorbar指定的颜色，默认：None;
◐capsize:标量，可选，在点中，决定errorbar长度； error_kw:字典，可选，
◐orientation:{'vertical','horizontal'},可选，条的方向
◐log:布尔，可选，若True,轴设置为对数尺度
◐kwargs: LineCollection properties.
'''





