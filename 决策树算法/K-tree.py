# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 15:50:23 2017

@author: Administrator
"""

#计算给定数据集的香农熵
from math import log
import operator

def calcShannonEnt(dataSet):
    numEntries=len(dataSet) #获得数据条数
    labelCounts={} #创建数据字典，其键值是数据最后一列的数值（字典中成员："键:值"）
    for featVec in dataSet: #按行遍历数据集
        currentLabel=featVec[-1] #目前类别标签：取当前数据向量的最后一列的数值,currentLabel是键
        if currentLabel not in labelCounts.keys():#若当前类别标签不在字典的键的列表里
            labelCount[currentLabel]=0 #扩展字典（创建"键:值"，）将当前健值加入字典，健值是0
        labelCounts[currentLabel]+=1 #否则健值 +1。每个健值记录当前类别出现次数
    shannonEnt=0.0  #熵初值0
    for k in labelCounts:
        prob=float(labelCounts[key])/numEntries #计算第k个类别所占比例，看作其出现的概率
        shannonEnt -= prob*log(prob,2)#累加求和，即当前数据集的熵
    return shannonEnt
    
#按照给定特征划分数据集
def spliDataSet(dataSet,axis,value):#待划分数据集，划分数据集的特征，需要返回的特征的值
    retDataSet=[] #创建新的列表对象
    for featVec in dataSet:#遍历数据集
        if featVec[axis]==value:#若某样例在此特征上的值就是value
            reducedFeatVec=featVec[:axis]#取此样例的第 0--axis-1个
            reducedFeatVec.extend(featVec[axis+1:])#取此样例的第 axis+1个到最后。  即抽取符合特征的样例
            retDataSet.append(reducedFeatVec)#将抽取的符合特征的样例放入新建列表中
    return retDataSet
        
#选择最好的数据划分集
def chooseBestFeatureToSplit():
    numFeatures=len(dataSet[0])-1 #计算特征向量的维度(特征的个数)，即数组dataSet的第一行(dataSet[0])的元素个数 -1，减的是标签列
    baseEntropy=calcShannonEnt(dataSet)#计算整个数据集的原始熵
    bestInfoGain=0.0;bestFeature=-1#初始信息增益0，初始最优划分特征是列号为-1的特征
    for i in range(numFeatures):#按列遍历特征向量
        featList=[example[i] for example in dataSet] #将数据集中的所有第i个特征值放入List中
        uniqueVals=set(featList) #使用集合数据类型,即利用集合元素的互异性
        newEntropy=0.0
        for value in uniqueVals:#遍历当前特征值中的所有唯一属性值，对每个属性值划分一次数据集
            subDataSet=splitDataSet(dataSet,i,value)#划分数据集
            prob=len(subDataSet)/float(len(dataSet))#计算在第i个特征上取值value的数据在数据集中所占比例
            newEntropy += prob*calcShannonEnt(subDataSet)#计算数据集的新熵值
        inforGain=bestEntroty-newEntropy#计算信息增益
        if (inforGain > bestInforGain):#计算最好的信息增益
            bestInforGian=inforGain
            bestFeature=i
    return bestFeature
        
 

#类节点的标签不唯一时，多数表决
def majorityCnt(classList)#使用分类名称的列表
classCount={}#定义字典(存储每个类别标签出现的频率)
for vote in classList:#遍历
    if vote not in classCount.keys():#若类别标签不在字典中
        classCount[vote]=0#扩建字典，此标签健值为0
    classCount[vote]+=1#健值+1
sortedClassCount=sorted(classCount.iteritems(),key=operator.itemgetter(1),reverse=Ture)#操作健值排序字典
#sorted函数:返回一个经过排序的列表
#classCount.iteritems()：返回一个迭代器
#operator.itemgetter: operator模块提供的itemgetter函数用于获取对象的哪些维的数据，参数为一些序号（即需要获取的数据在对象中的序号），下面看例子。
# #reverse:reverse：是一个布尔值。如果设置为True，列表元素将被降序排列，默认为升序排列。
return sortedClassCount[0][0]#返回出现次数最多的分类名称


#创建数的函数代码
def createTree(dataSet,labels):
    classList=[example[-1] for example in dataSet]#获取数据集的标签列表
    if classList.count(classList[0])==len(calssList):#.count(x):计算列表中x出现的次数，若所有的类别标签相同(classList[0]:标签列表第一个元素)
        return classList[0]#直接返回该类标签
    if len(dataSet[0])==1:#使用所有标签，仍然有数据不能唯一的划分到某类。dataSet[0]：数据集第一行
        return majorityCnt(classList)#多数表决
    bestFeat=chooseBestFeatureToSplit(dataSet)#调用函数选择最优划分特征,返回 i:第几个特征
    bestFeatLabel=labels[bestFeat]#？？？
    myTree={bestFeatLabel:{}}
    del(labels[bestFeat])#del用于list列表及字典操作，删除一个或者连续几个元素也可以删除字典指定的key
    featValues=[example[bestFeat] for example in dataSet]#获取第i个特征在数据集上的所有属性值
    uniqueVals=set(featValues)#用集合表示，互异性
    for value in uniqueVals:
        subLabels=labels[:]#复制类标签
        myTree[bestFeatLabel][value]=createTree(splitDataSet(dataSet,bestFeat,value),subLabels)
    return myTree


#使用决策树的分类函数
def classify(inputTree,featLabels,testVec):
    firstStr=inputTree.keys()[0]
    secondDict=inputTree[firstStr]
    featIndex=featLabels.index(firstStr)#将标签字符串转换为索引，查找第一个匹配firstStr变量的元素。
    for key in secondDict.keys():
        if testVec[featIndex] == 'key'
            if type(secondDict[key]).__name__=='dict':
                classLabel=classify(secondDict[key],featLabels,testVec)
            else: classLabel=secondDict[key]
    return classLabel
    
    
#使用pickle模块存储决策树
def storeTree(inputTree,filename):
    import pickle
    fw=open(filename,'w')
    pickle.dump(inputTree,fw)
    fw.close()
    
def grabTree(filename):
    import pickle
    fr=open(filename)
    return pickle.load(fr)
    
    
    
            
        
    
    


     