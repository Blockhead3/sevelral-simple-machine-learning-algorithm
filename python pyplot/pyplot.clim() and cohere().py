# -*- coding: utf-8 -*-
"""
Created on Wed Oct 04 11:46:03 2017

@author: cabbage
"""

'''matplotlib.pyplot.clim(vmin=None.vmax=None)
设置当前图形的颜色限制，
    clim(0,0.5):应用于所有子图
若vmin或vmax有一个为None,图像的min/max分别应用于色标
若要设置多个图像的clim：for im in gca.get_images(): im.set_clim(0.0.05)
'''

'''matplotlib.pyplot.cohere((x, y, NFFT=256, Fs=2, Fc=0,\
detrend=<function detrend_none>, window=<function window_hanning>,\
 noverlap=0, pad_to=None, sides='default', scale_by_freq=None, hold=None, data=None, **kwargs)
绘制x与y之间的幅度平方相干性（相干性是归一化的交叉谱密度）
参数：
    Fs:标量，采样频率，它被用来计算傅里叶频率，freqs，默认2
    window:标量或对象，长度NFFT（非规则采样快速傅里叶变换）的一个函数或向量，默认window_hanning()
    sides:['default'|'onesided'|'twosided'],指定返归频谱的哪边
    pad_to:integer,在执行FFT(快速傅氏变换算法)时，数据段被填充的点的个数
    NFFT:integer,用于FFT的每个块中使用的数据点的数量。
    detrend:{'default','constant','mean','linear','none'},或标量，在fft前应用于每个部分的一个函数，用于去除平均或线性的线性趋势
    scale_by_freq:布尔，可选，指定产生的密度值是否应该按照缩放频率缩放
    noverlap:integer,块之间的重叠点个数。默认值为0(no overlap)
    Fc:interger,x(默认值为0)的中心频率，它抵消了绘图的x区段，以反映在获得信号时使用的频率范围，然后对基带进行过滤和采样。
    kwargs:控制Line2D属性的参数
'''

#例（计算两信号的相干性）
import numpy as np
import matplotlib.pyplot as plt


plt.subplots_adjust(wspace=0.5)#再两子图之间制造一点额外空间

dt=0.01
t=np.arange(0,30,dt)
nse1=np.random.randn(len(t))#白噪声1
nse2=np.random.randn(len(t))#白噪声2
r=np.exp(-t/0.05)

cnse1=np.convolve(nse1,r,mode='same')*dt #convolve:卷积。有色噪声1
cnse2=np.convolve(nse2,r,mode='same')*dt #有色噪声2

#具有相干部分与随机部分的两个信号
s1=0.01*np.sin(2*np.pi*10*t)+cnse1
s2=0.01*np.sin(2*np.pi*10*t)+cnse2

plt.subplot(211)
plt.plot(t,s1,t,s2)
plt.xlim(0,5)
plt.xlabel('time')
plt.ylabel('s1 and s2')
plt.grid(True)

plt.subplot(212)
cxy,f=plt.cohere(s1,s2,256,1./dt)
plt.ylabel('coherence')
plt.show()


