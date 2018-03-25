# -*- coding: utf-8 -*-
"""
Created on Wed Oct 04 09:08:00 2017

@author: cabbage
"""

'''matplotlib.pyplot.cla() 清除当前轴
'''

'''matplotlib.pyplot.clf()清空当前的图
'''

'''matplotlib.pyplot.close(*args)关闭图窗口
close():关闭目前窗口
close(h):关闭窗口h
close(num)关闭窗口num
close(name):name是字符串，关闭以此字符串为名的窗口
close('all'):关闭所有窗口
'''


'''matplotlib.pyplot.clabel(CS,8args,**kwargs)标记等高线图
调用签名：clabel(cs,**kwargs),给cs中等高线加标签，cs是一个等高线集
         clabel(cs,v,**kwargs),只标记在v中列出的等高线
参数：fontsize: 尺度大小
     colors:None(每个标签的颜色与对应等高线一样)
            string(eg:colors='r',标签是红色)
            tuple(string,float,rgb,etc),不同的标签指定不同颜色
     inline:控制是否删除标签下的线，默认True
     inline_spacing:   
     fmt:标签的格式字符串，默认：%1.3f
     manual:True(等高线标签将使用鼠标点击手动放置)，
     rightside_up:True(标签旋转将永远是正负90度)
     use_clabeltext:True(ClabelText类(而不是matplotlib . text)用于创建标签)
'''

#例（画等高线）
import matplotlib
import numpy as np
import matplotlib.cm as cm
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

matplotlib.rcParams['xtick.direction']='out'#使用rcParams修改参数
matplotlib.rcParams['ytick.direction']='out'

delta=0.025
x=np.arange(-3.0,3.0,delta)
y=np.arange(-2.0,2.0,delta)
X,Y=np.meshgrid(x,y)
Z1=mlab.bivariate_normal(X,Y,1.0,1.0,0.0,0.0)#四个数分别是x,y的方差，均值
Z2=mlab.bivariate_normal(X,Y,1.5,0.5,1,1)
Z=10.0*(Z2-Z1)

#使用默认颜色创建一个简单的等高线，online参数控制标签是画在等高线上，还是将线移到标签下面
plt.figure()
CS=plt.contour(X,Y,Z)
plt.clabel(CS,inline=1,fontsize=10)
plt.title('Simplest default with labels')


#手动放置等高线标签，
plt.figure()
CS=plt.contour(X,Y,Z)
manual_locations=[(-1,-1.4),(-0.62,-0.7),(-2,0.5),(1.7,1.2),(2.0,1.4),(2.4,1.7)]
plt.clabel(CS,inline=1,fontsize=10,manual=manual_locations)
plt.title('labels at selected locations')


#使等高线统一颜色
matplotlib.rcParams['contour.negative_linestyle']='dashed'
plt.figure()
CS=plt.contour(X,Y,Z,6,colors='k')
plt.clabel(CS,fontsize=9,inline=1)
plt.title('Single color-neative contours dashed')


#设置负等高线为实线而不是虚线
matplotlib.rcParams['contour.negative_linestyle']='solid'
plt.figure()
CS=plt.contour(X,Y,Z,6,colors='k')
plt.clabel(CS,fontsize=9,inline=1)
plt.title('Single color-negative contours solid')

#指定颜色
plt.figure()
CS=plt.contour(X,Y,Z,6,linewidth=np.arange(.5,4,.5),colors=('r','green','blue',(1,1,0),'#afeeee','0.5'))
plt.clabel(CS,fontsize=9,inline=1)
plt.title('Crazy lines')

#用色图指定颜色
plt.figure()
im=plt.imshow(Z,interpolation='bilinear',origin='lower',cmap=cm.gray,extent=(-3,3,-2,2))
levels=np.arange(-1.2,1.6,0.2)
CS=plt.contour(Z,levels,origin='lower',linewidth=2,extent=(-3,3,-2,2))

#加厚0等高线
zc=CS.collections[6]
plt.setp(zc,linewidth=4)
plt.clabel(CS,levels[1::2],inline=1,fmt='%1.1f',fontsize=14)#levels[1::2]; label every second level

#绘制等高线的颜色条
CB=plt.colorbar(CS,shrink=0.8,extend='both')
plt.title('Lines with colorbar')
#plt.hot()#改变色图
plt.flag()


#给图加个颜色条
CBI=plt.colorbar(im,orientation='horizontal',shrink=0.8)
#这使得原来的colorbar看起来有点不合适，让我们改进它的位置
l,b,w,h=plt.gca().get_position().bounds
ll,bb,ww,hh=CB.ax.get_position().bounds
CB.ax.set_position([ll,b+0.1*h,ww,h*0.8])

plt.show()
     
