# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 10:39:25 2017

@author: Cabbage
"""

#CART算法的实现代码
from numpy import *


def loadDataSet(fileName):
    dataMat=[]
    fr=open(fileName)
    for line in fr.readlines():
        curLine=line.strip().split('\t')
        fltLine=map(float,curLine)#将每行映射成浮点
        dataMat.append(fltLine)
    
    return dataMat
    
    
def binSplitDataSet(dataSet,feature,value):#feature:待切分的特征，value:该特征的某个值
    mat0=dataSet[nonzero(dataSet[:,feature] > value)[0],:]#nonzero(dataSet[:,feature]>value)[0]:返回dataSet中feature列中大于value的元素所在的行 i,
    mat1=dataSet[nonzero(dataSet[:,feature] <= value)[0],:]
    return mat0,mat1
    
def regLeaf(dataSet):#returns the value used for each leaf
    return mean(dataSet[:,-1])#目标变量的均值
    

def regErr(dataSet):
    return val(dataSet[:,-1])*shape(dataSet)[0]#目标便量的样本方差，等价于均方差乘以样例的个数


def chooseBestSplit(dataSet,leafType=regLeaf,errType=regErr,ops=(1,4)):
    tolS=ops[0]
    tolN=ops[1]
    if len(set(dataSet[:,-1].T.tolist()[0])) == 1:#所有值相等
        return None,leafType(dataSet)#无需划分，返回均值
    m,n=shape(dataSet)
    S=errType(dataSet)
    bestS=inf
    bestIndex=0
    bestValue=0
    for featIndex in range(n-1):#遍历每一个特征
        for splitVal in set((dataSet[:,featIndex].T.tolist())[0]):#每个特征值
            mat0,mat1=binSplitDataSet(dataSet,featIndex,splitVal)#划分为两份
            if (shape(mat0)[0]<tolN) or (shape(mat1)[0]<tolN):
                continue
            newS=errType(mat0)+errType(mat1)
            if newS<bestS:
                bestIndex=featIndex
                bestValue=splitVal
                bestS=newS
    if (S-bestS)<tolS:#满足条件
        return None,leafType(dataSet)
    mat0,mat1=binSplitDataSet(dataSet,bestIndex,bestValue)#最优切分
    if (shape(mat0)[0]<tolN) or (shape(mat1)[0]<tolN):
        return None,leafType(dataSet)
    return bestIndex,bestValue

             
def createTree(dataSet,leafType=regLeaf,errType=regErr,ops=(1,4)):
    feat,val=chooseBestSplit(dataSet,leafType,errType,ops)
    if feat==None:
        return val
    retTree={}
    retTree['spInd']=feat
    retTree['spVal']=val
    lSet,rSet=binSplitDataSet(dataSet,feat,val)
    retTree['left']=createTree(lSet,leafType,errType,ops)
    retTree['right']=createTree(rSet,leafType,errType,ops)
    return retTree
    

#回归树剪枝函数
def isTree(obj):#测试输入变量是否是一颗树
    return (type(obj).__name__ =='dict')
    
def getMean(tree):#找到两个叶节点，计算其平均值
    if isTree(tree['right']):
        tree['right']=getMean(tree['right'])
    if isTree(tree['left']):
        tree['left']=getMean(tree['left'])
    return (tree['left']+tree['right'])/2.0
    
def prune(tree,testData):
    if shape(testData)[0]==0:
        return getMean(tree)
    if (isTree(tree['right']) or isTree(tree['left'])):
        lSet,rSet=binSplitDataSet(testData,tree['spInd'],tree['spVal'])
    if isTree(tree['left']):
        tree['left']=prune(tree['left'],lSet)
    if isTree(tree['right']):
        tree['right']=prune(tree['right'],rSet)
    if not isTree(tree['left']) and not isTree(tree['right']):
        lSet,rSet=binSplitDataSet(testData,tree['spInd'],tree['spVal'])
        errorNoMerge=sum(power(lSet[:,-1]-tree['left'],2))+sum(power(rSet[:,-1]-tree['right'],2))
        treeMean=(tree['left']+tree['right'])/2.0
        errorMerge=sum(power(testData[:,-1]-treeMean,2))
        if errorMerge < errorNoMerge:
            print "merging"
        else:
            return tree
    else:
        return tree
    
#模型树的叶节点生成函数 
def linearSolve(dataSet):
    m,n=shape(dataSet)
    X=mat(ones((m,n)))
    Y=mat(ones((m,1)))
    X[:,1:n]=dataSet[:,0:n-1]
    Y=dataSet[:,-1]
    xTx=X.T*X
    if linalg.det(xTx)==0:
        raise NameError('This matrix is singular,cannot do inverse,\n try increasing the second value of ops')
    ws=xTx.I*(X.T*Y)
    return ws,X,Y
    
def modelLeaf(dataSet):
    ws,X,Y=linearSolve(dataSet)
    return ws
    
def modelErr(dataSet):
    ws,X,Y=linearSolve(dataSet)
    yHat=X*ws
    return sum(power(Y-yHat,2))

#用树回归进行预测的代码
def regTreeEval(model,inDat):
    return float(model)
    
def modelTreeEval(model,inDat):
    n=shape(inDat)[1]
    X=mat(ones((1,n+1)))
    X[:,1:n+1]=inDat
    return float(X*model)
    
def treeForeCast(tree,inData,modelEval=regTreeEval):
    if not isTree(tree):
        return modelEval(tree,inData)
    if inData[tree['spInd']]>tree['spVal']:
        if isTree(tree['left']):
            return treeForeCast(tree['left'],inData,modelEval)
        else:
            return modelEval(tree['left'],inData)
    else:
        if isTree(tree['right']):
            return treeForeCast(tree['right'],inData,modelEval)
        else:
            return modelEval(tree['right'],inData)
        
def createForeCast(tree,testData,modelEval=regTreeEval):
    m=len(testData)
    yHat=mat(zeros((m,1)))
    for i in range(m):
        yHat[i,0]=treeForeCast(tree,mat(testData[i]),modelEval)
    return yHat
   
    