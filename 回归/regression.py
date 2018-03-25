# -*- coding: utf-8 -*-
"""
Created on Wed Nov 08 19:25:16 2017

@author: Cabage
"""

#标准回归方程的导入函数
from numpy import *

def loadDataSet(fileName):
    numFeat=len(open(fileName).readline().split('\t'))-1#文件的每行的最后一个值是目标值
    dataMat=[]
    labelMat=[]
    fr=open(fileName)
    for line in fr.readlines():
        lineArr=[]
        curLine=line.strip().split('\t')
        for i in range(numFeat):
            lineArr.append(float(curLine[i]))
        dataMat.append(lineArr)
        labelMat.append(float(curLine[-1]))
    return dataMat,labelMat
    
def standRegres(xArr,yArr):#用于计算最佳拟合曲线
    xMat=mat(xArr)
    yMat=mat(yArr).T
    xTx=xMat.T*xMat
    if linalg.det(xTx)==0.0: #判断x'x的行列式是否为0
       print "This matrix is singular,cannot do inverse"
       return 
    ws=xTx.I*(xMat.T*yMat)# xTx.I:是xTx的逆
    return ws


#局部加权线性回归
def lwlr(testPoint,xArr,yArr,k=1.0):#每次预测需要事先给testPoint对应的数据子集，然后为其赋予一定权重
    xMat=mat(xArr)
    yMat=mat(yArr).T
    m=shape(xMat)[0]
    weights=mat(eye((m)))#创建对角矩阵，对角线元素全为1
    for j in range(m):
        diffMat=testPoint-xMat[j,:]#与xMat的第j行相减
        weights[j,j]=exp(diffMat*diffMat.T/(-2*k**2))#计算每个样本点对应的权重
        xTx=xMat.T*(weights*xMat)
        if linalg.det(xTx)==0.0:
            print "This matrix is singular,cannot do inverse"
            return 
        ws=xTx.I*(xMat.T*(weights*yMat))#计算出回归系数
        return testPoint*ws
        
def lwlrTest(testArr,xArr,yArr,k=1.0):#为数据集中的每一个点调用lwlt()函数
    m=shape(testArr)[0]
    yHat=zeros(m)
    for i in range(m):
        yHat[i]=lwlr(testArr[i],xArr,yArr,k)
    return yHat
        
def lwlrTestPlot(xArr,yArr,k=1.0):  #same thing as lwlrTest except it sorts X first
    yHat = zeros(shape(yArr))       #easier for plotting
    xCopy = mat(xArr)
    xCopy.sort(0)
    for i in range(shape(xArr)[0]):
        yHat[i] = lwlr(xCopy[i],xArr,yArr,k)
    return yHat,xCopy

        
def rssError(yArr,yHatArr):
    return ((yArr-yHatArr)**2).sum()
    
#岭回归
def ridgeRegres(xMat,yMat,lam=0.2):#计算回归系数
    xTx=xMat.T*xMat
    denom=xTx+eye(shape(xMat)[1])*lam
    if linalg.det(denom)==0:
        print "This matrix is singular,cannot do inverse"
        return 
    ws=denom.I*(xMat.T*yMat)
    return ws
    
def ridgeTest(xArr,yArr):
    xMat=mat(xArr)
    yMat=mat(yArr).T
    yMean=mean(yMat,0)#对各列求均值
    xMeans=mean(xMat,0)
    xVar=var(xMat,0)
    xMat=(xMat-xMeans)/xVar#数据标准化
    numTestPts=30
    wMat=zeros((numTestPts,shape(xMat)[1]))#构造numTestPts行，shape(xMat)[1]列的矩阵
    for i in range(numTestPts):#在30个不同λ下调用ridgeRegres()函数
        ws=ridgeRegres(xMat,yMat,exp(i-10))
        wMat[i,:]=ws.T
    return wMat

 
def regularize(xMat):#regularize by columns
    inMat = xMat.copy()
    inMeans = mean(inMat,0)   #calc mean then subtract it off
    inVar = var(inMat,0)      #calc variance of Xi then divide by it
    inMat = (inMat - inMeans)/inVar
    return inMat
    
def stageWise(xArr,yArr,eps=0.01,numIt=100):#eps:每次迭代需要调整的步长；numIt:迭代的次数
    xMat=mat(xArr)
    yMat=mat(yArr).T
    yMean=mean(yMat,0)
    yMat=yMat-yMean
    xMat=regularize(xMat)#均值为0，方差为1的标准化处理
    m,n=shape(xMat)
    returnMat=zeros((numIt,n))
    ws=zeros((n,1))#用于储存w的值
    wsTest=ws.copy()
    wsMax=ws.copy()
    for i in range(numIt):
        print ws.T
        lowestError=inf
        for j in range(n):#对每一个特征
            for sign in [-1,1]:
                wsTest=ws.copy()
                wsTest[j]+=eps*sign
                yTest=xMat*wsTest
                rssE=rssError(yMat.A,yTest.A)#调用rssError()函数，计算误差
                if rssE<lowestError:
                    lowestError=rssE
                    wsMax=wsTest
        ws=wsMax.copy()
        returnMat[i,:]=ws.T
    return returnMat
    
                    
               
#购物信息的获取函数
from time import sleep
import json
import urllib2

def searchForSet(retX,retY,setNum,yr,numPce,origPrc):
    sleep(10)
    #myAPIstr='get from code.google.com'
    myAPIstr='get from code.baidu.com'
    #searchURL='http://www.googleapis.com/shopping/search/v1/public/products?key=%s&country=US&q=lego+%d&alt=json'%(myAPIstr,setNum)
    searchURL='http://www.baidu.com/shopping/search/v1/public/products?key=%s&country=US&q=lego+%d&alt=json'%(myAPIstr,setNum)
    
    pg=urllib2.urlopen(searchURL)
    retDict=json.loads(pg.read())
    for i in range(len(retDict['items'])):
        try:
            currItem=retDict['items'][i]
            if currItem['product']['condition']=='new':
                newFlag=1
            else:
                newFlag=0
            listOfInv=currItem['product']['inventories']
            for item in listOfInv:
                sellingPrice=item['price']
                if sellingPrice > origPrc*0.5:
                    print "%d\t%d\t%d\t%f\t%f"%(yr,numPce,newFlag,origPrc,sellingPrice)
                    retX.append([yr,numPce,newFlag,origPrc])
                    retY.append(sellingPrice)
        except:
            print 'problem with item %d'%i
            
def setDataCollect(retX,retY):
    searchForSet(retX,retY,8288,2006,800,49.99)
    searchForSet(retX,retY,10030,2002,3096,269.99)
    searchForSet(retX,retY,10179,2007,5195,499.99)
    searchForSet(retX,retY,10181,2007,3428,199.99)
    searchForSet(retX,retY,10189,2008,5922,299.99)
    searchForSet(retX,retY,10196,2009,3263,149.99)
    
    
#交叉验证测试岭回归
def crossValidation(xArr,yArr,numVal=10):
    m=len(yArr)
    indexList=range(m)
    errorMat=zeros((numVal,30))#选择了30个不同的 λ，交叉验证的次数是10，
    for i in range(numVal):
        trainX=[]
        trainY=[]
        testX=[]
        testY=[]
        random.shuffle(indexList)#对indexList进行混洗，达到测试卷、训练集随机选取的效果
        for j in range(m):
            if j<m*0.9:
                trainX.append(xArr[indexList[j]])#90%的作为训练集
                trainY.append(yArr[indexList[j]])
            else:
                testX.append(xArr[indexList[j]])#10%的作为测试集
                testY.append(yArr[indexList[j]])
    wMat=ridgeTest(trainX,trainY)
        for k in range(30):
            matTestX=mat(testX)
            matTrainX=mat(trainX)
            meanTrain=mean(matTrainX,0)
            VarTrain=var(matTrainX,0)
            matTestX=(matTestX-meanTrain)/VarTrain#标准化处理
            yEst=matTestX*mat(wMat([k,:]).T+mean(trainY))
            errorMat[i,k]=rssError(yEst.T.A,array(testY))
    meanErrors=mean(errorMat,0)
    minMean=float(min(meanErrors))
    bestWeights=wMat[nonzero(meanErrors=minMeans)]
    xMat=mat(xArr)
    yMat=mat(yArr).T
    meanX=mean(xMat,0)
    varX=var(xMat,0)
    unReg=bestWeights/varX
    print "the best modle from Ridge Regression is:\n",unReg
    print "with constant term:\n",-1*sum(multiply(meanX,unRge))+mean(yMat)
    
    
            
            
        
            
    
               
            
   
    
    
 
    
    
        
    