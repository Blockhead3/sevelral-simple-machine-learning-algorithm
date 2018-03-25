# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 20:26:53 2017

@author: Administrator
"""

#os模块中的函数listdir()用于返回指定的文件夹包含的文件或文件夹的名字的列表。这个列表以字母顺序
#语法：os.listdir(path), path是需要列出的目录路径，返回指定路径下的文件和文件夹列表
import os
#help(os.listdir)
dirs=os.listdir('trainingDigits')
for file in dirs:
    print file


