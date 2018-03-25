# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 16:40:33 2017

@author: Administrator
"""

import regTrees
from numpy import *

'''myDat=regTrees.loadDataSet('ex00.txt')
myMat=mat(myDat)
regTrees.createTree(myMat)'''

'''myDat2=regTrees.loadDataSet('ex2.txt')
myMat2=mat(myDat2)
print regTrees.createTree(myMat2)

myTree=regTrees.createTree(myMat2,ops=(0,1))
myDataTest=regTrees.loadDataSet('ex2test.txt')
myMat2Test=mat(myDataTest)
regTrees.prune(myTree,myMat2Test)'''


'''myMat2=mat(regTrees.loadDataSet('exp2.txt'))
regTrees.createTree(myMat2,regTrees.modelLeaf,regTrees.modelErr,(1,10))'''

from Tkinter import *
root=Tk()
myLabel=Label(root,text='hello world')
myLabel.grid
