# -*- coding: utf-8 -*-
"""
Created on Fri Oct 06 15:01:14 2017

@author: Administrator
"""

'''matplotlib.pyplot.cool()设置默认的colormap以cool并应用于当前图像
matplotlib.pyplot.copper()设置默认的colormap以copper并应用于当前图像
'''

'''matplotlib.pyplot.delaxes(*args)移除当前图形的轴
'''

'''matplotlib.pyplot.disconnect(cid)分开调用cid
'''

'''matplotlib.pyplot.draw()重画当前图
'''

'''matplotlib.pyplot.csd(x, y, NFFT=256, Fs=2, Fc=0, detrend=mlab.detrend_none,
                        window=mlab.window_hanning, noverlap=0, pad_to=None,
                        sides='default', scale_by_freq=None, return_line=None, **kwargs)
绘制交叉谱密度  
'''

#例（计算两个信号的交叉谱密度）
import numpy as np
import matplotlib.pyplot as plt

fig,(ax1,ax2)=plt.subplots(2,1)
fig.subplots_adjust(hspace=0.5)#设置两个子图之间的空间

dt=0.01
t=np.arange(0,30,dt)
nse1=np.random.randn(len(t))#白噪声1
nse2=np.random.randn(len(t))#白噪声2
r=np.exp(-t/0.05)

cnse1=np.convolve(nse1,r,mode='same')*dt #有色噪声1
cnse2=np.convolve(nse2,r,mode='same')*dt #有色噪声2

s1=0.01*np.sin(2*np.pi*10*t)+cnse1
s2=0.01*np.sin(2*np.pi*10*t)+cnse2

ax1.plot(t,s1,t,s2)
ax1.set_xlim(0,5)
ax1.set_xlabel('time')
ax1.set_ylabel('s1 and s2')
ax1.grid(True)

cxy,f=ax2.csd(s1,s2,256,1./dt)
ax2.set_ylabel('CSD(ab)')

plt.show()
