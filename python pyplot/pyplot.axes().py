# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30 21:10:22 2017

@author: Administrator
"""

''' matplotlib.pyplot.axes(*args,**kwargs)向图中添加一个轴
◆axes()通过它本身创建了一个默认的完整子图(111)窗口轴。
◆axes(rect,facecolor='w'),其中,在归一化(0,1)单元中，rect=[left,bottom,width,height]，facecolor是轴的背景颜色，默认白
◆axes(h)  h是轴实例，使h是目前的轴    
kwarg:facecolor(颜色，轴的背景色)
      frameon([True|False],是否展示框架（帧）)
      sharex(当前轴与其他轴共享xaxis属性)
      sharey(当前轴与其他轴共享xaxis属性)
      polar([True|False],是否用极坐标)
      aspect([str|num],[' equal '，' auto ']或数字。如果一个数字在屏幕空间中的x单位/ y单位的比率)
'''

#例
import matplotlib.pyplot as plt
import numpy as np

#创造画图用的数据
dt=0.001
t=np.arange(0.0,10.0,dt)
r=np.exp(-t[:1000]/0.05)#脉冲响应
x=np.random.randn(len(t))
s=np.convolve(x,r)[:len(x)]*dt #有色噪声,convolve--卷积函数库

#默认主子图是（111）
plt.plot(t,s)
plt.axis([0,1,1.1*np.amin(s),2*np.amax(s)])
plt.xlabel('time(s)')
plt.ylabel('current(nA)')
plt.title('Gaussian colored noise')

#主图上的一个嵌入图
a=plt.axes([.65,.6,.2,.2])
n,bins,patches=plt.hist(s,400,normed=1)
plt.title('probability')
plt.xticks([])
plt.yticks([])

#主图上另一个嵌入图
a=plt.axes([0.2,0.6,.2,.2])
plt.plot(t[:len(r)],r)
plt.title('Impulse response')
plt.xlim(0,0.2)
plt.xticks([])
plt.yticks([])

plt.show()    

#例

t=np.arange(0.01,5.0,0.01)
s1=np.sin(2*np.pi*t)
s2=np.exp(-t)
s3=np.sin(4*np.pi*t)

ax1=plt.subplot(311)
plt.plot(t,s1)
plt.setp(ax1.get_xticklabels(),fontsize=6)

ax2=plt.subplot(312,sharex=ax1)#共享x
plt.plot(t,s2)
plt.setp(ax2.get_xticklabels(),visible=False)

ax3=plt.subplot(313,sharex=ax1,sharey=ax1)#共享x,y
plt.plot(t,s3)
plt.xlim(0.01,5.0)

plt.show()