# -*- coding: utf-8 -*-
"""
Created on Fri Oct 06 11:05:24 2017

@author: cabbage
"""

'''matplotlib.pyplot.colorbar(mappable=None,cax=None,ax=None,**kw) 给图增加一个颜色条

colorbar(**kwargs)
colorbar(mappable, **kwargs)
colorbar(mappable, cax=cax, **kwargs)
colorbar(mappable, ax=ax, **kwargs)
参数：
    mappable:colorbar应用的图像，mappable是colorbar()方法的必须参数，是colorbar()函数的可选参数
    cax:None|画colorbar的图对象
    ax:None|父图--一个新的colorbar轴来源
    use_gridspec:False |如果cax是None，则创建一个新的cax作为坐标轴的实例。如果ax是Subplot的实例，use_gridspec是True，
                        那么cax是使用grid_spec模块创建的子图实例
'''

'''matplotlib.pyplot.colors()这是一个没有任何功能的函数，它可以帮助您在matplotlib如何处理颜色方面提供帮助。
✎用单个字母表示
   ‘b’---blue
   ‘g’--green
   ‘r’---red
   ‘c’---cyan(蓝绿色)
   ‘m’---magenta(品红)
   ‘y’--yellow
   ‘k’---black
   ‘w’---white
✎用html十六进制字符串表示
   color='#eeefff'
   title('Is this the best color?', color='#afeeee')
✎传递一个R,G,B元组，其中R,G,B范围是[0,1]
   subplot(111,facecolor=(0.1843,0.3198,0.3098))
✎用合法的html名称
   color = 'red'；color = 'burlywood'；color = 'chartreuse'
'''


     
