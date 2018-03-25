# -*- coding: utf-8 -*-
"""
Created on Fri Oct 06 12:36:31 2017

@author: cabbage
"""

'''matplotlib.pyplot.contour(*args,**kwargs)画等高线
contour()--画等高线
contourf()--画填充的等高线
调用签名：
       contour(Z):绘制数组z的等高线图，水平值自动选取
       contour(X,Y,Z):X,Y指定表面的(x,y)坐标
       contour(Z,N);contour(X,Y,Z,N):画等高线到N个自动选择的水平
       contour(Z,V);contour(X,Y,Z,V):根据序列V中指定的值绘制等高线，V必须是递增顺序的
       contourf(...,V):在V的值之间填充len(V)- 1区域，V必须是递增顺序的。
       contour(Z,**kwargs):用关键自变量控制等高线
**kwargs:
    corner_mask:[True|False|'legacy'],启用/禁用角落掩蔽，只有当Z是一个masked数组时才有效果
    colors:[None|string|(mpl_colors)]
    alpha:float,alpha混合值
    cmap:[None|Colormap]:一个cm Colormap实例或None
    norm:[None|Normalize]matplotlib.colors.Normalize实例用于对颜色生成数据值。
    vmin,vmax[None|scalar],若非None，这些值都将用于matplotlib.colors.Normalize实例，
                           覆盖基于级别的默认颜色扩展
    levels:[level1,level1,...,leveln]一个浮点数的列表，指示水平曲线绘制
    origin: [None|'upper'|'lower'|'image'],若None，Z的第一个值对应于左下角，位置(0,0)
'''

#例（画等高线、色条及带标签的等高线）
import matplotlib
import numpy as np
import matplotlib.cm as cm
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

matplotlib.rcParams['xtick.direction']='out'
matplotlib.rcParams['ytick.direction']='out'

delta=0.025
x=np.arange(-3.0,3.0,delta)
y=np.arange(-2.0,2.0,delta)
X,Y=np.meshgrid(x,y)
Z1=mlab.bivariate_normal(X,Y,1.0,1.0,0.0,0.0)
Z2=mlab.bivariate_normal(X,Y,1.5,0.5,1,1)
Z=10.0*(Z2-Z1)

plt.figure()
CS=plt.contour(X,Y,Z)
plt.clabel(CS,inline=1,fontsize=10)
plt.title('Simplest default with labels')

plt.figure()
CS=plt.contour(X,Y,Z)
manual_locations=[(-1,-1.4),(-0.62,-0.7),(-2,0.5),(1.7,1.2),(2.0,1.4),(2.4,1.7)]
plt.clabel(CS,inline=1,fontsize=10,manual=manual_locations)
plt.title('labels at selected locations')


matplotlib.rcParams['contour.negative_linestyle'] = 'dashed'
plt.figure()
CS=plt.contour(X,Y,Z,6,colors='k')
plt.clabel(CS,fontsize=9,inline=1)
plt.title('Single color-negative contours dashed')


matplotlib.rcParams['contour.negative_linestyle'] = 'solid'
plt.figure()
CS=plt.contour(X,Y,Z,6,colors='k')
plt.clabel(CS,fontsize=9,inline=1)
plt.title('Single color-negative contours solid')

plt.figure()
CS=plt.contour(X,Y,Z,6,linewidths=np.arange(.5,4,2),colors=('r','green','blue',(1,1,0),'#afeeee','0.5'))
plt.clabel(CS,fontsize=6,inline=1)
plt.title('Crazy me')


plt.figure()
im=plt.imshow(Z,interpolation='bilinear',origin='lower',cmap=cm.gray,extent=(-3,3,-2,2))
levels=np.arange(-1.2,1.6,0.2)
CS=plt.contour(Z,levels,origin='lower',linewidths=2,extent=(-3,3,-2,2))
zc=CS.collections[6]
plt.setp(zc,linewidth=4)
plt.clabel(CS,levels[1::2],inline=1,fmt='%1.1f',fontsize=14)
CB=plt.colorbar(CS,shrink=0.8,extend='both')
plt.title('Lines with colorbar')
plt.flag()
CBI=plt.colorbar(im,orientation='horizontal',shrink=0.8)
l,b,w,h=plt.gca().get_position().bounds
ll,bb,ww,hh=CB.ax.get_position().bounds
CB.ax.set_position([ll,b+0.1*h,ww,h*0.8])

plt.show()


#例（画填充的等高线）
import numpy as np
import matplotlib.pyplot as plt

origin='lower'
#origin='upper'
delta=0.025
x=y=np.arange(-3.0,3.01,delta)
X,Y=np.meshgrid(x,y)
Z1=plt.mlab.bivariate_normal(X,Y,1.0,1.0,0.0,0.0)
Z2=plt.mlab.bivariate_normal(X,Y,1.5,0.5,1,1)
Z=10*(Z1-Z2)
nr,nc=Z.shape
Z[-nr//6:,-nc//6:]=np.nan

Z=np.ma.array(Z)
Z[:nr//6,:nc//6]=np.ma.masked

interior=np.sqrt((X**2)+(Y**2))<0.5
Z[interior]=np.ma.masked

CS=plt.contourf(X,Y,Z,10,cmap=plt.cm.bone,origin=origin)
CS2=plt.contour(CS,levels=CS.levels[::2],colors='r',origin=origin)
plt.title('Nonsense(3 masked regions)')
plt.xlabel('word length anomaly')
plt.ylabel('sentence length anomaly')

cbar=plt.colorbar(CS)
cbar.ax.set_ylabel('verbosity coefficient')
cbar.add_lines(CS2)

plt.figure()
levels=[-1.5,-1,-0.5,0,0.5,1]
CS3=plt.contourf(X,Y,Z,levels,colors=('r','g','b'),origin=origin,extend='both')
CS3.cmap.set_under('yellow')
CS3.cmap.set_over('cyan')
CS4=plt.contour(X,Y,Z,levels,colors=('k',),linewidths=(3,),origin=origin)
plt.title('Listed colors (3 masked regions)')
plt.clabel(CS4,fmt='%2.1f',colors='w',fontsize=14)
plt.colorbar(CS3)
extends=["neither","both","min","max"]
cmap=plt.cm.get_cmap("winter")
cmap.set_under("magenta")
cmap.set_over("yellow")

fig,axs=plt.subplots(2,2)
fig.subplots_adjust(hspace=0.3)
for ax,extend in zip(axs.ravel(),extends):
    cs=ax.contourf(X,Y,Z,levels,cmap=cmap,extend=extend,origin=origin)
    fig.colorbar(cs,ax=ax,shrink=0.9)
    ax.set_title("extend=%s"%extend)
    ax.locator_params(nbins=4)
    
plt.show()


#例（corner_mask=False和corner_mask=True之间的区别）
import numpy as np
import matplotlib.pyplot as plt

x,y=np.meshgrid(np.arange(7),np.arange(10))
z=np.sin(0.5*x)*np.cos(0.52*y)

mask=np.zeros_like(z,dtype=np.bool)
mask[2,3:5]=True
mask[3:5,4]=True
mask[7,2]=True
mask[5,0]=True
mask[0,6]=True
z=np.ma.array(z,mask=mask)

corner_masks=[False,True]
for i,corner_mask in enumerate(corner_masks):
    plt.subplot(1,2,i+1)
    cs=plt.contourf(x,y,z,corner_mask=corner_mask)
    plt.contour(cs,colors='k')
    plt.title('corner_mask={0}'.format(corner_mask))
    
    plt.grid(c='k',ls='-',alpha=0.3)
    plt.plot(np.ma.array(x,mask=mask),y,'ro')
    
plt.show()







    