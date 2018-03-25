# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 17:20:44 2017

@author: Administrator
"""

'''matplotlib.pyplot.angle_spectrum(x,Fs=None,Fc=None,window=None,pad_to=None,sides=None,hold=None,**kwargs)画临界角谱'''
#调用格式：angle_spectrum(x, Fs=2, Fc=0,  window=mlab.window_hanning,pad_to=None, sides='default', **kwargs)
#计算x的角度谱(包裹的相位谱)，将数据添加到pad_to的长度，并将窗口函数窗口应用于信号
#x--一维数组或序列（包含数据的数组或序列）
#Fs--标量，采样频率(每个时间单位的样本)。它被用来计算傅里叶频率，freqs，在周期单位。默认值为2。
#window--可调用或对象，一个离散傅里叶变换长度的函数或向量，如果一个函数作为参数传递，它必须以一个数据段作为参数，并返回该部分的窗口版本。
#sides--（默认值|单边|双边），指定要返回谱的哪一边，默认值为实数数据返回一边，为复数据返回双边；
#pad_to--整型，在执行FFT时，数据段被填充的点的个数
#Fc--整型，x的中心频率(默认为0)，当信号被获取，然后过滤和被采样到基带时，它会抵消绘图的x区段，以反映所使用的频率范围。
#**kwargs--关键字参数控制2维线性属性，


#例3(matplotlib.pyplot.angle_spectrum)
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)
dt=0.01
Fs=1/dt
t=np.arange(0,10,dt)#第一个参数开始值、第二个参数结束值（不包括）、第三个参数步长（每个元素间的间隔）
nse=np.random.randn(len(t))
r=np.exp(-t/0.05)

cnse=np.convolve(nse,r)*dt#返回离散，两个一维序列的线性卷积。卷积算子通常是信号处理中看到的，它 模型的线性时不变系统对信号的影响.在概率理论，两独立随机变量之和 根据他们个人的 分布的卷积分布
cnse=cnse[:len(t)]
s=0.1*np.sin(2*np.pi*t)+cnse

plt.subplot(321)
plt.plot(t,s)

plt.subplot(323)
plt.magnitude_spectrum(s,Fs=Fs)

plt.subplot(324)
plt.magnitude_spectrum(s,Fs=Fs,scale='dB')

plt.subplot(325)
plt.angle_spectrum(s,Fs=Fs)

plt.subplot(326)
plt.phase_spectrum(s,Fs=Fs)

plt.show()