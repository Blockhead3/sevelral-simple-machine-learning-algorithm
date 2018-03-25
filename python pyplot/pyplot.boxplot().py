# -*- coding: utf-8 -*-
"""
Created on Sun Oct 01 20:58:02 2017

@author: Administrator
"""

'''matplotlib.pyplot.box(on=None)
打开或关闭坐标轴，可以是布尔或字符串，“on”或“off”。
如果没有，切换状态.'''


#箱线图（Boxplot）也称箱须图（Box-whisker Plot），是利用数据中的五个统计量：最小值、上分位数（Q1）、中位数、下分位数(Q3)、最大值
#来描述数据的一种方法，它也可以粗略地看出数据是否具有有对称性
'''matplotlib.pyplot.boxplot()
为数组x中为每一列或为序列x中每个向量做一个盒子和须图，这个盒子从数据的下四分位数到上四分位数，
中间有一条线。胡须从盒子里伸出来显示数据的范围。Flier点指的是那些在胡须末端经过的点。
参数：
✎x:向量的数组或序列，（输入数据）
✎notch:布尔，可选，True(画锯齿状盒子)，False(矩形盒子)，notches表示中位数周围的置信区间(CI)。
✎sym:字符串，可选，flier点的默认符号，'':不显示；None:'b+'
✎vert:布尔，可选，True(默认，使箱垂直)，False(一切水平画)
✎whis:float,序列或字符，IQR--四分位距(Q3-Q1),上须扩展到Q3+whis*IQR,下须扩展到Q1-whis*IQR，此区间（两条直线）外的点被视为异常点
✎bootstrap:int,optional,指定是否引导置信区间在notched box地块的中值附近
✎usermedians:array-like,optional,第一维度与x一致，
✎zorder:标量，可选，设置箱线图的层次
✎meanline:布尔，可选，True:使均值成为一条线，横跨box的宽度
✎autorange:bool,optional,True(数据分布使得第25和第75百分位相等)，
✎manage_xtick:bool,optional,若是函数，调整xlim和xtick
✎labels:序列，可选，每个数据集的标签，维度与x一致
✎widths:标量或数组类，为用一个标量或一个序列每个盒子的宽度
✎positions:数组类，可选，设置盒子的位置，刻度和范围根据位置自动设置
'''

#例（演示绘制盒子的格式制定）
import numpy as np
import matplotlib.pyplot as plt

#伪造数据
np.random.seed(937)
data=np.random.lognormal(size=(37,4),mean=1.5,sigma=1.75)
labels=list('ABCD')
fs=10#字体大小

# demonstrate how to toggle the display of different elements:
fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(6, 6), sharey=True)
axes[0, 0].boxplot(data, labels=labels)
axes[0, 0].set_title('Default', fontsize=fs)

axes[0, 1].boxplot(data, labels=labels, showmeans=True)#showmeans:展示算数平均值
axes[0, 1].set_title('showmeans=True', fontsize=fs)

axes[0, 2].boxplot(data, labels=labels, showmeans=True, meanline=True)#meanline:将均值画成一条线
axes[0, 2].set_title('showmeans=True,\nmeanline=True', fontsize=fs)

axes[1, 0].boxplot(data, labels=labels, showbox=False, showcaps=False)#showbox:显示中间的盒子；showcaps:显示须的帽子
tufte_title = 'Tufte Style \n(showbox=False,\nshowcaps=False)'
axes[1, 0].set_title(tufte_title, fontsize=fs)

axes[1, 1].boxplot(data, labels=labels, notch=True, bootstrap=10000)#notch:锯齿状，
axes[1, 1].set_title('notch=True,\nbootstrap=10000', fontsize=fs)

axes[1, 2].boxplot(data, labels=labels, showfliers=False)
axes[1, 2].set_title('showfliers=False', fontsize=fs)

for ax in axes.flatten():
    ax.set_yscale('log')
    ax.set_yticklabels([])

fig.subplots_adjust(hspace=0.4)
plt.show()


# demonstrate how to customize the display different elements:
boxprops = dict(linestyle='--', linewidth=3, color='darkgoldenrod')
flierprops = dict(marker='o', markerfacecolor='green', markersize=12,
                  linestyle='none')
medianprops = dict(linestyle='-.', linewidth=2.5, color='firebrick')
meanpointprops = dict(marker='D', markeredgecolor='black',
                      markerfacecolor='firebrick')
meanlineprops = dict(linestyle='--', linewidth=2.5, color='purple')

fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(6, 6), sharey=True)
axes[0, 0].boxplot(data, boxprops=boxprops)
axes[0, 0].set_title('Custom boxprops', fontsize=fs)

axes[0, 1].boxplot(data, flierprops=flierprops, medianprops=medianprops)
axes[0, 1].set_title('Custom medianprops\nand flierprops', fontsize=fs)

axes[0, 2].boxplot(data, whis='range')
axes[0, 2].set_title('whis="range"', fontsize=fs)

axes[1, 0].boxplot(data, meanprops=meanpointprops, meanline=False,
                   showmeans=True)
axes[1, 0].set_title('Custom mean\nas point', fontsize=fs)

axes[1, 1].boxplot(data, meanprops=meanlineprops, meanline=True,
                   showmeans=True)
axes[1, 1].set_title('Custom mean\nas line', fontsize=fs)

axes[1, 2].boxplot(data, whis=[15, 85])
axes[1, 2].set_title('whis=[15, 85]\n#percentiles', fontsize=fs)

for ax in axes.flatten():
    ax.set_yscale('log')
    ax.set_yticklabels([])

fig.suptitle("I never said they'd be pretty")
fig.subplots_adjust(hspace=0.4)
plt.show()





















