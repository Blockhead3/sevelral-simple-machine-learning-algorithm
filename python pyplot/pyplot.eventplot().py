# -*- coding: utf-8 -*-
"""
Created on Fri Oct 06 18:57:35 2017

@author: cabbage
"""

'''matplotlib.pyplot.eventplot(positions, orientation='horizontal', lineoffsets=1,\
         linelengths=1, linewidths=None, colors=None, linestyles='solid', hold=None, data=None, **kwargs)
在指定的位置绘制相同的平行线
参数：
orientation:['horizontal'|'vertical'],horizontal(线条会垂直排列成行),vertical(线条将是水平的,排列成纵队)
lineoffsets:float or array like containing floats
linelengths:float or array like containing floats
linewidths:float or array like containing floats
colors:必须是一个RGBA元组序列或这样的序列列表
linestyles:[ ‘solid’ | ‘dashed’ | ‘dashdot’ | ‘dotted’ ] or an array of these values
'''

#例
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
matplotlib.rcParams['font.size']=8.0

np.random.seed(0)#设置随机种子
data1=np.random.random([6,50])#制造随机数据
#为每个位置设置不同颜色
colors1=np.array([[1,0,0],
                  [0,1,0],
                  [0,0,1],
                  [1,1,0],
                  [1,0,1],
                  [0,1,1]])
#为每组位置设置不同的线属性
lineoffsets1=np.array([-15,-3,1,1.5,6,10])
linelengths1=[5,2,1,1,3,1.5]

fig=plt.figure()

#绘制水平方向
ax1=fig.add_subplot(221)
ax1.eventplot(data1,colors=colors1,lineoffsets=lineoffsets1,linelengths=linelengths1)

#绘制垂直方向
ax2=fig.add_subplot(223)
ax2.eventplot(data1,colors=colors1,lineoffsets=lineoffsets1,linelengths=linelengths1,orientation='vertical')

#制造另一组随机数据
data2=np.random.gamma(4,size=[60,50])
colors2=[[0,0,0]]
lineoffsets2=1
linelengths2=1

ax1=fig.add_subplot(222)
ax1.eventplot(data2,colors=colors2,lineoffsets=lineoffsets2,linelengths=linelengths2)

ax2=fig.add_subplot(224)
ax2.eventplot(data2,colors=colors2,lineoffsets=lineoffsets2,linelengths=linelengths2,orientation='vertical')

plt.show()           