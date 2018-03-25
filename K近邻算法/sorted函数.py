# -*- coding: utf-8 -*-
"""
Created on Tue Sep 05 16:33:45 2017

@author: Administrator
"""
#sorted函数： 返回一个经过排序的列表
help(sorted)
#sorted(iterable, cmp=None, key=None, reverse=False)
#参数解释 iterable:iteralbe指的是能够一次返回它的一个成员的对象，即可迭代的对象。
        # cmp:指定一个定制的比较函数，这个函数接收两个参数（iterable的元素），如果第一个参数小于第二个参数，返回一个负数；如果第一个参数等于第二个参数，返回零；如果第一个参数大于第二个参数，返回一个正数。默认值为None。
        #key:指定一个接收一个参数的函数，这个函数用于从每个元素中提取一个用于比较的关键字。默认值为None
       #reverse:reverse：是一个布尔值。如果设置为True，列表元素将被降序排列，默认为升序排列。
#列表排序
a=[4,5,3,6,7,2,1]
print(sorted(a))
#关键字函数
str1=sorted("This is a test string from Andrew".split(),key=str.lower)
print(str1)

student_tuples = [('Jerry', 'A', 15), ('Tom', 'C', 12),('Bill', 'B', 10)]  
sort_tuples = sorted(student_tuples, key=lambda student: student[2])  # sort by age, that is the third element of tuple  
print sort_tuples

#operator模块中的函数
import operator
student_tuples = [('Jerry', 'A', 15), ('Tom', 'C', 12),('Bill', 'B', 10)]  
opr_sort_tuples = sorted(student_tuples, key=operator.itemgetter(2))  
print opr_sort_tuples 

student_tuples = [('Jerry', 'A', 15), ('Tom', 'B', 12),('Bill', 'B', 10)]  
opr_sort_tuples = sorted(student_tuples, key=operator.itemgetter(1,2))  
print opr_sort_tuples 

#将学生记录按成绩降序排序、按年龄升序排列。先按年龄排序，再按成绩排序。
student_tuples = [('Jerry', 'C', 15), ('Tom', 'B', 12),('Bill', 'B', 10)]  
age_asc = sorted(student_tuples, key=operator.itemgetter(2))  
print age_asc  
score_desc = sorted(age_asc, key=operator.itemgetter(1), reverse=True)  
print score_desc 