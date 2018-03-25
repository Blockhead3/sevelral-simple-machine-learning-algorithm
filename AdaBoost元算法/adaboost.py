# -*- coding: utf-8 -*-
"""
Created on Thu Nov 02 14:15:27 2017

@author: Cabadge
"""

from numpy import *
def loadSimpData():
    datMat=matrix([[1.,2.1],
                   [2.,1.1],
                   [1.3,1.],
                   [1.,1.],
                   [2.,1.]])
    classLabels=[1.0,1.0,-1.0,-1.0,1.0]
    return datMat,classLabels
  
#单层决策树生成函数  
def stumpClassify(dataMatrix,dimen,threshVal,threshIneq):#定义分类方法
    retArray=ones((shape(dataMatrix)[0],1))#shape(dataMatrix)[0]:dataMatrix的行数,retArray是一列
    if threshIneq=='It':
        retArray[dataMatrix[:,dimen]<=threshVal]=-1.0#dataMatrix[:,dimen]:矩阵dataMatrix的第dimen列（从0开始）
                                                     #此列中各数值，若有小于或等于阈值的（如第2行的数<阈值），则对应的retArray的行（第2行）的位置是-1
    else:
        retArray[dataMatrix[:,dimen]>threshVal]=-1.0
    return retArray

    
def buildStump(dataArr,classLabels,D):#构建决策树桩
    dataMatrix=mat(dataArr)
    labelMat=mat(classLabels).T
    m,n=shape(dataMatrix)
    numSteps=10.0
    bestStump={}#最优决策树桩
    bestClasEst=mat(zeros((m,1)))
    minError=inf
    for i in range(n):#对每一列，(在数据集的所有特征上遍历)
        rangeMin=dataMatrix[:,i].min()
        rangeMax=dataMatrix[:,i].max()
        stepSize=(rangeMax-rangeMin)/numSteps
        for j in range(-1,int(numSteps)+1):#计算设置11个阈值，对每个阈值
            for inequal in ['It','gt']:
                threshVal=(rangeMin+float(j)*stepSize)
                predictedVals=stumpClassify(dataMatrix,i,threshVal,inequal)#调用此函数，得出一个分类结果
                errArr=mat(ones((m,1))) 
                errArr[predictedVals==labelMat]=0
                weightedError=D.T*errArr#加权错误率
                #print "split:dim %d,thresh %.2f,thresh inequal:%s,the weighted error is %.3f"%(i,threshVal,inequal,weightedError)
                if weightedError<minError:
                    minError=weightedError
                    bestClasEst=predictedVals.copy()
                    bestStump['dim']=i
                    bestStump['thresh']=threshVal
                    bestStump['ineq']=inequal
    return bestStump,minError,bestClasEst
                    
  
#基于单层决策树的AdaBoost训练过程
def adaBoostTrainDS(dataArr,classLabels,numIt=40):
    weakClassArr=[]
    m=shape(dataArr)[0]
    D=mat(ones((m,1))/m)#1/m
    aggClassEst=mat(zeros((m,1)))#用于记录每个每个数据点的类别估计累计值
    for i in range(numIt):
        bestStump,error,classEst=buildStump(dataArr,classLabels,D)
        print "D:",D.T
        alpha=float(0.5*log((1.0-error)/max(error,1e-16)))#max(error,le-16):确保无错误时，不会溢出
        bestStump['alpha']=alpha#将alpha添加到字典中
        weakClassArr.append(bestStump)#将字典添加到列表中，该字典包含分类所需所有信息
        print "classEst:",classEst.T#当前的分类结果
        expon=multiply(-1*alpha*mat(classLabels).T,classEst)
        D=multiply(D,exp(expon))
        D=D/D.sum()#更新权重向量D
        aggClassEst+=alpha*classEst#∑amGm(x),Gm(x)是第m次循环产生的个体学习器，am是其对应的权重
        print "aggClassEst:",aggClassEst.T
        aggError=multiply(sign(aggClassEst)!=mat(classLabels).T,ones((m,1)))#错误率累加计算
        errorRate=aggError.sum()/m#集成学习器的错误率
        print "total error:",errorRate,"\n"
        if errorRate==0.0:
            break
    #return weakClassArr
    return weakClassArr,aggClassEst#多个弱学习器组成的数组
            
        
        
#AdaBoost分类函数
def adaClassify(datToClass,classifierArr):#datToClass:待分类样例 classifierArr:多个弱学习器组成的数组
    dataMatrix=mat(datToClass)
    m=shape(datToClass)[0]
    aggClassEst=mat(zeros((m,1)))
    for i in range(len(classifierArr)):
        classEst=stumpClassify(dataMatrix,classifierArr[i]['dim'],classifierArr[i]['thresh'],classifierArr[i]['ineq'])
        aggClassEst+=classifierArr[i]['alpha']*classEst#加模型
        print aggClassEst
    return sign(aggClassEst)#决策函数
    
       
    
#自适应数据加载函数
def loadDataSet(fileName):
    numFeat=len(open(fileName).readline().split('\t'))
    dataMat=[]
    labelMat=[]
    fr=open(fileName)
    for line in fr.readlines():
        lineArr=[]
        curLine=line.strip().split('\t')
        for i in range(numFeat-1):
            lineArr.append(float(curLine[i]))
        dataMat.append(lineArr)
        labelMat.append(float(curLine[-1]))
    return dataMat,labelMat

#ROC曲线的绘制及AUC计算函数
def plotROC(predStrengths,classLabels):#predStrengths:分类器的预测强度
    import matplotlib.pyplot as plt
    cur=(1.0,1.0)#保留绘制光标的位置
    ySum=0.0#用于计算AUC值
    numPosClas=sum(array(classLabels==1.0))#正例的数目
    yStep=1/float(numPosClas)#确定y坐标上的步长（在(0--1)区间上绘制）
    xStep=1/float(len(classLabels)-numPosClas)#确定x轴步长
    sortedIndicies=predStrengths.argsort()#得到预测强度的排序索引
    fig=plt.figure()
    fig.clf()
    ax=plt.subplot(111)
    for index in sortedIndicies.tolist()[0]: #tolist():将数组或矩阵转换成列表
        if classLabels[index]==1.0:#若标签为1，沿y轴方向下降一个步长，即降低真阳率
            delX=0
            delY=yStep
        else:
            delX=xStep
            delY=0
            ySum+=cur[1]#所有小矩形的高度累加，最后乘以xStep(小矩形的宽)，得到总面积AUC
        ax.plot([cur[0],cur[0]-delX],[cur[1],cur[1]-delY],c='b')
        cur=(cur[0]-delX,cur[1]-delY)#更新cur的值
    ax.plot([0,1],[0,1],'b--')
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('ROC curve for AdaBoost Horse Colic Detection System')
    ax.axis([0,1,0,1])
    plt.show()
    print "the Area Under the Curve is:",ySum*xStep
    

        
    
    
                  
                    
                
        
        
        
        
    