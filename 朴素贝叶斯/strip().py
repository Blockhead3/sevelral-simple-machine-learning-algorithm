# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 15:38:46 2017

@author: Administrator
"""

#str.strip([chars]):方法用于移除字符串头尾指定的字符（默认为空格）。
#参数：chars:移除字符串头尾指定的字符

str="0000this is stri!!000000"
print str.strip('0')#移除两端的0

a='   123'
print a.strip()#移除两端空格

b='\t\tabc'
print b.strip()#空白符包括：'\n','\r','\t',''.

c='sdff\r\n'
print c.strip()#空白符包括：'\n','\r','\t',''.

d='123abc'
print d.strip('21')
print d.strip('12')#移除两端指定的'12'


#split()通过指定分隔符对字符串进行切片，如果参数num 有指定值，则仅分隔 num 个子字符串
#语法：str.split(str="", num=string.count(str)).
#参数：
''' str -- 分隔符，默认为所有的空字符，包括空格、换行(\n)、制表符(\t)等。
    num -- 分割次数 '''
    