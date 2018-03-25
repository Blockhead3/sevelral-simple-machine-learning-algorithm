# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 18:22:43 2017

@author: Administrator
"""
#使用文本注解绘制树节点
import matplotlib.pyplot as plt#使用matplotlib注解功能绘制图形
#定义文本框和箭头格式
decisionNode=dict(boxstyle="sawtooth",fc="0.8")#sawtooth:文本框的边缘是波浪类型,fc:控制文 本框内颜色深浅
leafNode=dict(boxstyle="round4",fc="0.8")
arrow_args=dict(arrowstyle="<-")#箭头符号
#绘制带箭头的注解
def plotNode(nodeTxt,centerPt,parentPt,nodeType): #执行绘画功能，nodeTxt--文本要显示的内容，centerPt--文本的中心位置，parentPt--起始位置，nodeType--节点类型
    createPlot.ax1.annotate(nodeTxt,xy=parentPt,xycoords='axes fraction',xytext=centerPt,textcoords='axes fraction',\
    va="center",ha="center",bbox=nodeType,arrowprops=arrow_args)
    #xy=parentpt--箭头开始的位置，xytext--注解内容的位置，若该值为None，注释内容放在xy处。xycoords与textcoords--是坐标xy与xytext的说明，
    #bbox--文本的边框形状，arrowprops--设置箭头形状（字典类型）
def createPlot():
    fig=plt.figure(1,facecolor='white')#创建新图形，背景白色
    fig.clf()#清空绘图区
    createPlot.ax1=plt.subplot(111,frameon=False)
    #createPlot.ax1为全局变量，绘制图像的句柄，subplot为定义了一个绘图，
    #111表示figure中的图有1行1列，即1个，最后的1代表第一个图 
    #frameon表示是否绘制坐标轴矩形
    plotNode('决策节点',(0.5,0.1),(0.1,0.5),decisionNode)
    plotNode('叶节点',(0.8,0.1),(0.3,0.8),leafNode)
    plt.show()
    
#构造注解树
#获取叶节点的数目和树的层数
def getNumLeafs(myTree):#遍历整棵树，累计叶子节点的个数
    numLeafs=0
    firstStr=myTree.keys()[0]#获得第一个key值（根节点）'no surfacing'
    secondDict=myTree[firstStr]#获得value值 ，即键'no surfacing'对应的值--{0: 'no', 1: {'flippers': {0: 'no', 1: 'yes'}}}是一个字典
    for key in secondDict.keys():#dict.keys()--获取键的列表
        if type(secondDict[key]).__name__=='dict':#若该子节点是字典类型。如果字典secondDict中的键对应的值，是字典类型，则该节点是判断节点。
            numLeafs += getNumLeafs(secondDict[key])#递归调用getNumLeafs()函数
        else: numLeafs += 1#若该子节点不是字典型，即是叶节点，叶子数 +1
    return numLeafs
 
   
def getTreeDepth(myTree):#计算遍历过程中判断节点的个数
    maxDepth=0
    firstStr=myTree.keys()[0]
    secondDict=myTree[firstStr]
    for key in secondDict.keys():
        if type(secondDict[key]).__name__=='dict':
            thisDepth=1+getTreeDepth(secondDict[key])
        else: thisDepth = 1
        if thisDepth > maxDepth:
            maxDepth = thisDepth
    return maxDepth
    
def retrieveTree(i):
    listOfTrees=[{'no surfacing':{0:'no',1:{'flippers':{0:'no',1:'yes'}}}},\
               {'no surfacing':{0:'no',1:{'flippers':{0:{'head':{0:'no',1:'yes'}},1:'no'}}}}]
    return listOfTrees[i]
    
#plotTree函数
def plotMidText(cntrPt,parentPt,txtString):#两个节点之间的线上写上字
    xMid=(parentPt[0]-cntrPt[0])/2.0+cntrPt[0]
    yMid=(parentPt[1]-cntrPt[1])/2.0+cntrPt[1]
    createPlot.ax1.text(xMid,yMid,txtString)
    
def plotTree(myTree,parentPt,nodeTxt):#计算树的宽和高
    numLeafs=getNumLeafs(myTree)
    depth=getTreeDepth(myTree)
    firstStr=myTree.keys()[0]
    cntrPt=(plotTree.xOff+(1.0+float(numLeafs))/2.0/plotTree.totalW,plotTree.yOff)
    #plotTree.xOff和plotTree.yOff--追踪已经绘制的节点位置，以及放置下一个节点的位置。
    #plotTree.totalW--储存树的宽度，用于计算判断节点的位置
    plotMidText(cntrPt,parentPt,nodeTxt)
    plotNode(firstStr,cntrPt,parentPt,decisionNode)#标记子节点的属性值
    secondDict=myTree[firstStr]
    plotTree.yOff=plotTree.yOff-1.0/plotTree.totalD#plotTree.totalD--储存树的深度
    for key in secondDict.keys():
        if type(secondDict[key]).__name__=='dict':
            plotTree(secondDict[key],cntrPt,str(key))
        else:
         plotTree.xOff=plotTree.xOff+1.0/plotTree.totalW# x轴的绘制范围0.0--1.0，y轴的绘制范围是0.0--1.0
         plotNode(secondDict[key],(plotTree.xOff,plotTree.yOff),cntrPt,leafNode)
         plotMidText((plotTree.xOff,plotTree.yOff),cntrPt,str(key))
    plotTree.yOff=plotTree.yOff+1.0/plotTree.totalD
    
def createPlot(inTree):
    fig=plt.figure(1,facecolor='white')
    fig.clf()
    axprops=dict(xticks=[],yticks=[])
    createPlot.ax1=plt.subplot(111,frameon=False,**axprops)
    plotTree.totalW=float(getNumLeafs(inTree))
    plotTree.totalD=float(getTreeDepth(inTree))
    plotTree.xOff=-0.5/plotTree.totalW;plotTree.yOff=1.0
    plotTree(inTree,(0.5,1.0),'')
    plt.show()
    
        
        
    
    
    
    
    
    
        
    

        
        
    
    
    
    
    
   
