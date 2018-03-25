# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 19:04:07 2017

@author: Administrator
"""

#python 中一切皆对象,只有一些保留的关键词不是对象，如'if','+'
a=257
print type(a)#对象类型，这里是"int"
print id(a)#id()函数：返回对象的内存地址

#函数是对象
def foo():
    print "hi"

print type(foo)
print id(foo)

#type函数本身也是对象
print type(type),id(type)

#定义 class基本形式如下:

'''class ClassName(ParentClass):
    """class docstring"""
    def method(self):
        return '''
#✎ class关键词在最前面
#✎ ClassName通常使用CamelCase记法
#✎ 括号里的ParentClass用来表示继承关系
#✎ 冒号不能少       
#✎ """"""中的内容可省略
#✎ 方法定义和函数定义十分相似，但多了一个self参数表示这个对象本身
#✎ class中的方法要进行缩进        
class Forest(object):
    pass

import numpy as np
print np.info(Forest)

forest=Forest()
print forest

#可直接添加属性
forest.trees=np.zeros((150,150),dtype=bool)
print forest.trees

  
