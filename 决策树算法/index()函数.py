# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 15:04:40 2017

@author: cabbage
"""


# index() 方法检测字符串中是否包含子字符串 str ，如果指定 beg（开始）和 end（结束） 范围
#str.index(str, beg=0, end=len(string))

#str – 指定检索的字符串 
#beg – 开始索引，默认为0。 
#end – 结束索引，默认为字符串的长度。


t=tuple('Allen')
print t
#t.index('a')
print t.index('e')#返回e在t中的索引
print t.index('l')
print t.index('l',2)

str1='Tomorrow is National Day,the day after tomorrow is my birthday.'
str2='after'
print str1.index(str2)
print str1.index(str2,30)
print str1.index(str2,40)