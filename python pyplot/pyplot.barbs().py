# -*- coding: utf-8 -*-
"""
Created on Sun Oct 01 19:13:30 2017

@author: Administrator
"""

#画一个二维的倒钩(倒刺)
'''matplotlib.pyplot.barbs(*args,**kw)
调用特征：
barbs(u,v,**kw)
barbs(u,v,c,**kw)
barbs(x,y,u,v,**kw)
barbs(x,y,u,v,c,**kw)
参数：
X,Y:倒钩位置的x,y坐标，默认位置是barb的头
U,V:给出barb轴的x,y分量
C:一个可选数组，用于将颜色映射到倒钩（barbs）
length:点上barb的长度，默认9
pivot:['tip'|'middle']在格点的箭头部分;箭头绕着这一点旋转，因此得名枢轴。默认是'tip'
barbcolor:[color'|color sequence],指定barb的所有部分的颜色，除了flags
flagcolor:[color'|color sequence],指定barb上所有flags的颜色
sizes:一个系数字典，指定给定特征与barb的长度比例
fill_empty:一个flags是空的倒钩(圆)是否应该被填满旗的颜色
rounding:当分配barb组件时，一个flags表示向量大小是否应该四舍五入
barb_increments:增量词典，用于指定与barb的不同部分相关联的值。
flip_barb:要么是一个布尔flags，要么是一个布尔值数组
'''
#例（风羽图的展示）

import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(-5,5,5)
X,Y=np.meshgrid(x,x)
U,V=12*X,12*Y

data=[(-1.5,.5,-6,-6),
      (1,-1,-46,46),
      (-3,-1,11,-11),
      (1,1.5,80,80),
      (0.5,0.25,25,15),
      (-1.5,-0.5,-5,40)]
      
data=np.array(data,dtype=[('x',np.float32),('y',np.float32),
                          ('u',np.float32),('v',np.float32)])#data['x']是上面data中的第一列，依次下去
#定义参数，均匀网格
ax=plt.subplot(221) 
ax.barbs(X,Y,U,V)

#任一向量集合，延长它们，改变轴心点（它们绕其旋转的点）到中间
ax=plt.subplot(222)
ax.barbs(data['x'],data['y'],data['u'],data['v'],length=8,pivot='middle')

#显示均匀网格的映射，为空的barb填充圆圈，不四舍五入，改变某些尺度参数
ax=plt.subplot(223)
ax.barbs(X,Y,U,V,np.sqrt(U*U+V*V),fill_empty=True,rounding=False,\
         sizes=dict(empybarb=0.25,spacing=0.2,height=0.3))

#改变颜色以及对部分倒钩的增量
ax=plt.subplot(224)
ax.barbs(data['x'],data['y'],data['u'],data['v'],flagcolor='r',\
         barbcolor=['b','g'],barb_increments=dict(half=10,full=20,flag=100),\
         flip_barb=True)
         
#支持  Masked arrays   
masked_u=np.ma.masked_array(data['u'])
masked_u[4]=1000
masked_u[4]=np.ma.masked

#在第一个图中画，但点（0.5,0.25）消失
fig2=plt.figure()
ax=fig2.add_subplot(111)
ax.barbs(data['x'],data['y'],masked_u,data['y'],length=8,pivot='middle')

plt.show()

