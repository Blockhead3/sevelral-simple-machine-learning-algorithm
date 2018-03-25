# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 16:43:47 2017

@author: Administrator
"""

#split()函数：拆分字符串。通过指定分隔符对字符串进行切片，并返回分割后的字符串列表（list）
#os.path.split():按照路径将文件名和路径分割开

help(str.split)
#str.split(str="",num=string.count(str))[n]
#str:分隔符，默认为空格
#num:分割次数
#n:表示选取第几个分片
u="I like moving moving,you like too!"
print u.split(',')[0]
print u.split(',')[1]
print u.split('i')
print u.split('i')[3]
print u.split('i',2)

str="hello boy<[www.doiido.com]>byebye"
print str.split("[")[1].split("]")[0]
print str.split("[")[1].split("]")[0].split(".")


