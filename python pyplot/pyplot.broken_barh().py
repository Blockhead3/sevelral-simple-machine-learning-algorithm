# -*- coding: utf-8 -*-
"""
Created on Mon Oct 02 10:40:54 2017

@author: cabbage
"""

'''matplotlib.pyplot.broken_barh(xranges,yrange,hold=None,data=None,**kwargs)
#一组跨越yrange的横条，xrange的序列。
参数：
   xranges:序列，来自(xmin,xwidth)的序列
   yrange:来自(ymin,yidth)的序列
'''

#例（做一个“broken”的水平条形图）  

import matplotlib.pyplot as plt

fig,ax=plt.subplots()
ax.broken_barh([(110,30),(150,10)],(10,9),facecolors='blue')
ax.broken_barh([(10,50),(100,20),(130,10)],(20,9),facecolors=('red','yellow','green'))

ax.set_ylim(5,35)
ax.set_xlim(0,200)
ax.set_xlabel('seconds since start')
ax.set_yticks([15,25])
ax.set_yticklabels(['Bill','Jim'])
ax.grid(True)
ax.annotate('race interrupted',(61,25),xytext=(0.8,0.9),textcoords='axes fraction',arrowprops=dict(facecolor='black',shrink=0.05),fontsize=16,horizontalalignment='right',verticalalignment='top')


plt.show()
