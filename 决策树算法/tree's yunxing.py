# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 15:25:18 2017

@author: Administrator
"""

'''def createDataSet():
    dataSet=[[1,1,'yes'],[1,1,'yes'],[1,0,'no'],[0,1,'no'],[0,1,'no']]
    labels=['no surfacing',flippers]
    return dataSet,labels
    
import trees
myDat,labels=trees.createDataSet()
print myDat
print trees.calcShannonEnt(myDat)
myDat[0][-1]='maybe'
print myDat
print trees.calcShannonEnt(myDat)

import trees
myDat,labels=trees.createDataSet()
print myDat
print trees.splitDataSet(myDat,0,1)
print trees.splitDataSet(myDat,0,0)

import trees
myDat,labels=trees.createDataSet()
print trees.chooseBestFeatureToSplit(myDat)

import trees
myDat,labels=trees.createDataSet()
myTree=trees.createTree(myDat,labels)
print myTree'''


'''import treePlotter
print treePlotter.retrieveTree(1)
myTree=treePlotter.retrieveTree(0)
print myTree
print treePlotter.getNumLeafs(myTree)
print treePlotter.getTreeDepth(myTree)'''


'''import treePlotter
myTree=treePlotter.retrieveTree(0)
treePlotter.createPlot(myTree)

myTree['no surfacing'][3]='maybe'
print myTree
treePlotter.createPlot(myTree)'''


'''import trees
import treePlotter
myDat,labels=trees.createDataSet()
print labels
myTree=treePlotter.retrieveTree(0)
print myTree
print trees.classify(myTree,labels,[1,0])'''


import trees
import treePlotter
fr=open('lenses.txt')
lenses=[inst.strip().split('\t') for inst in fr.readlines()]
lensesLabels=['age','prescript','astigmatic','tearRate']
lensesTree=trees.createTree(lenses,lensesLabels)
lensesTree
treePlotter.createPlot(lensesTree)





