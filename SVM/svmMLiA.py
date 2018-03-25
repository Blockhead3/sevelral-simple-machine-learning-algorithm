# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 15:08:50 2017

@author: Administrator
"""
 
from numpy import *
from time import sleep



#SMO算法中的辅助函数
def loadDataSet(fileName):
    dataMat=[]
    labelMat=[]
    fr=open(fileName)
    for line in fr.readlines():
        lineArr=line.strip().split('\t')#分割
        dataMat.append([float(lineArr[0]),float(lineArr[1])])#取前两个数据
        labelMat.append(float(lineArr[2]))#取第三个数据，是标签
    return dataMat,labelMat#返回数据集合标签集
    
def selectJrand(i,m):#i:第一个alpha的下标，m:所有alpha的个数，与样例数个数一样多
    j=i
    while (j==i):
        j=int(random.uniform(0,m))#随机选取一个小标j
    return j
    
def clipAlpha(aj,H,L):#调整大于H或小于L的alpha值
    if aj>H:
        aj=H
    if L>aj:
        aj=L
    return aj
      

#简化的SMO算法
def smoSimple(dataMatIn,classLabels,C,toler,maxIter):#数据集、类别标签、常数C、容错率、推出前的最大循环次数
    dataMatrix=mat(dataMatIn)#转化成矩阵形式
    labelMat=mat(classLabels).transpose()
    b=0
    m,n=shape(dataMatrix)
    alphas=mat(zeros((m,1)))#构造一个alpha列矩阵，矩阵中元素初始化为0
    iter=0
    while (iter<maxIter):#外循环，当迭代次数小于最大迭代次数时
        alphaPairsChanged=0#用于记录alpha是否已进行优化
        for i in range(m):#内循环，对数据集中的每个数据向量
            fXi=float(multiply(alphas,labelMat).T*(dataMatrix*dataMatrix[i,:].T))+b    #multiply:对应元素相乘；'.T':矩阵转置；dataMatrix[i,:]:dataMatrix的第i(从0算起)行
            Ei=fXi-float(labelMat[i])#误差
            if ((labelMat[i]*Ei < -toler) and (alphas[i] < C))\
                 or ((labelMat[i]*Ei > toler) and (alphas[i] > 0)):#如果该数据向量可以被优化（不在边界上），labelMat[i]*Ei:yf(xi)-1
                j=selectuJrand(i,m)#随机选取另一个下标 j,这样就确定另一个数据向量
                fXj=float(multiply(alphas,labelMat).T*(dataMatrix*dataMatrix[j,:].T))+b
                Ej=fXj-float(labelMat[j])
                alphaIold=alphas[i].copy()
                alphaJold=alphas[j].copy()
                if (labelMat[i] != labelMat[j]):#计算L和H的值
                    L=max(0,alphas[j]-alphas[i])
                    H=min(C,C+alphas[j]-alphas[i])
                else:
                    L=max(0,alphas[j]+alphas[i]-C)
                    H=min(C,alphas[j]+alphas[i])#保证alpha在0和C之间
                if L==H:
                    print "L=H"
                    continue#若L=H，则不做任何改变，本次循环结束
                eta=2.0*dataMatrix[i,:]*dataMatrix[j,:].T-\
                        dataMatrix[i,:]*dataMatrix[i,:].T-\
                        dataMatrix[j,:]*dataMatrix[j,:].T
                if eta >= 0:
                    print "eta>=0"
                    continue
                alphas[j] -= labelMat[j]*(Ei-Ej)/eta#更新aj
                alphas[j]=clipAlpha(alphas[j],H,L)#调运clipAlpha函数
                if (abs(alphas[j]-alphaJold)<0.00001):#新旧值对比
                    print "j not moving enough"
                    continue
                alphas[i] += labelMat[j]*labelMat[i]*(alphaJold-alphas[j])#对i进行修改
                b1=b-Ei-labelMat[i]*(alphas[i]-alphaIold)*dataMatrix[i,:]*dataMatrix[i,:].T-\
                     labelMat[j]*(alphas[j]-alphaJold)*dataMatrix[i,:]*dataMatrix[j,:].T
                b2=b-Ej-labelMat[i]*(alphas[i]-alphaIold)*dataMatrix[i,:]*dataMatrix[j,:].T-\
                     labelMat[j]*(alphas[j]-alphaJold)*dataMatrix[j,:]*dataMatrix[j,:].T
                if (0<alphas[i]) and (C>alphas[i]):
                    b=b1
                elif (0<alphas[j]) and (C>alphas[j]):
                    b=b2
                else:
                    b=(b1+b2)/2.0
                alphaPairsChanged+=1
                print "iter:%d ,i: %d ,pairs changed %d"%(iter,i,alphaPairsChanged)
        if (alphaPairsChanged==0):
            iter+=1#外循环次数加
        else:
            iter=0
        print "iteration number:%d"%iter
    return b,alphas
    
                
                    
#完整版Platt SMO支持函数
                    
'''class optStruct: #误差缓存
    def __init__(self,dataMatIn,classLabels,C,toler):
        self.X=dataMatIn
        self.labelMat=classLabels
        self.C=C
        self.tol=toler
        self.m=shape(dataMatIn)[0]
        self.alphas=mat(zeros((self.m,1)))
        self.b=0
        self.eCache=mat(zeros(((self.m,2)))'''
        
        
def kernelTrans(X,A,kTup):
    m,n=shape(X)
    K=mat(zeros((m,1)))
    if kTup[0]=='lin':
        K=X*A.T
    elif kTup[0]=='rbf':
        for j in range(m):
            deltaRow=X[j,:]-A
            K[j]=deltaRow*deltaRow.T
        K = exp(K/(-1*kTup[1]**2)) 
    else:
        raise NameError('Houston we have a problem--That Kernel is not recognized')
    return K

class optStruct:
    def __init__(self,dataMatIn,classLabels,C,toler,kTup):
        self.X=dataMatIn
        self.labelMat=classLabels
        self.C=C
        self.tol=toler
        self.m=shape(dataMatIn)[0]
        self.alphas=mat(zeros((self.m,1)))
        self.b=0
        self.eCache=mat(zeros((self.m,2)))
        self.K=mat(zeros((self.m,self.m)))
        for i in range(self.m):
            self.K[:,i]=kernelTrans(self.X,self.X[i,:],kTup)
            
    
#计算E
def calcEk(oS,k):
       fXk=float(multiply(oS.alphas,oS.labelMat).T*oS.K[:,k]+oS.b)
       Ek=fXk-float(oS.labelMat[k])
       return Ek
        
def selectJ(i,oS,Ei):
        maxK=-1
        maxDeltaE=0
        Ej=0
        oS.eCache[i]=[1,Ei]
        validEcacheList=nonzero(oS.eCache[:,0].A)[0]#nonzers():返回非0数据的位置，oS.eCache[:,0]:矩阵oS.eCache的第一列，
        if (len(validEcacheList))>1:
            for K in validEcacheList:
                if K==i:
                    continue
                EK=calcEk(oS,K)
                deltaE=abs(Ei-EK)
                if (deltaE>maxDeltaE):
                    maxK=K
                    maxDeltaE=deltaE
                    Ej=EK
            return maxK,Ej
        else:
            j=selectJrand(i,oS.m)
            Ej=calcEk(oS,j)
        return j,Ej
        
def updateEk(oS,k):
    Ek=calcEk(oS,k)
    oS.eCache[k]=[1,Ek]
        
    
#完整Platt SMO算法中的优化例程
def innerL(i,oS):
    Ei=calcEk(oS,i)
    if ((oS.labelMat[i]*Ei<-oS.tol)and(oS.alphas[i]<oS.C))or((oS.labelMat[i]*Ei>oS.tol)and(oS.alphas[i]>0)):
        j,Ej=selectJ(i,oS,Ei)
        alphaIold=oS.alphas[i].copy()
        alphaJold=oS.alphas[j].copy()
        if (oS.labelMat[i]!=oS.labelMat[j]):
            L=max(0,oS.alphas[j]-oS.alphas[i])
            H=min(oS.C,oS.C+oS.alphas[j]-oS.alphas[i])
        else:
            L=max(0,oS.alphas[j]+oS.alphas[i]-oS.C)
            H=min(oS.C,oS.C+oS.alphas[j]+oS.alphas[i])
        if L==H:
            print "L=H"
            return 0
        eta=2.0*oS.K[i,j]-oS.K[i,i]-oS.K[j,j]
        if eta>=0:
            print "eta>=0"
            return 0
        oS.alphas[j]-=oS.labelMat[j]*(Ei-Ej)/eta
        oS.alphas[j]=clipAlpha(oS.alphas[j],H,L)
        updateEk(oS,j)
        if (abs(oS.alphas[j]-alphaJold)<0.00001):
            print "j not moving enough"
            return 0
        oS.alphas[i]+=oS.labelMat[j]*oS.labelMat[i]*(alphaJold-oS.alphas[j])
        updateEk(oS,i)
        b1=oS.b-Ei-oS.labelMat[i]*(oS.alphas[i]-alphaIold)*oS.K[i,i]-\
           oS.labelMat[j]*(oS.alphas[j]-alphaJold)*oS.K[i,j]
        b2=oS.b-Ej-oS.labelMat[i]*(oS.alphas[i]-alphaIold)*oS.K[i,j]-\
           oS.labelMat[j]*(oS.alphas[j]-alphaJold)*oS.K[j,j]
        if (0<oS.alphas[i])and(oS.C>oS.alphas[i]):
            oS.b=b1
        elif(0<oS.alphas[j])and(oS.C>oS.alphas[j]):
            oS.b=b2
        else:
            oS.b=(b1+b2)/2.0
        return 1
    else:
        return 0
        


#完整版完整Platt SMO的外循环代码
def smoP(dataMatIn, classLabels, C, toler, maxIter,kTup=('lin', 0)):    #full Platt SMO
    oS = optStruct(mat(dataMatIn),mat(classLabels).transpose(),C,toler, kTup)
    iter = 0
    entireSet = True; alphaPairsChanged = 0
    while (iter < maxIter) and ((alphaPairsChanged > 0) or (entireSet)):
        alphaPairsChanged = 0
        if entireSet:   #go over all
            for i in range(oS.m):        
                alphaPairsChanged += innerL(i,oS)
                print "fullSet, iter: %d i:%d, pairs changed %d" % (iter,i,alphaPairsChanged)
            iter += 1
        else:#go over non-bound (railed) alphas
            nonBoundIs = nonzero((oS.alphas.A > 0) * (oS.alphas.A < C))[0]
            for i in nonBoundIs:
                alphaPairsChanged += innerL(i,oS)
                print "non-bound, iter: %d i:%d, pairs changed %d" % (iter,i,alphaPairsChanged)
            iter += 1
        if entireSet: entireSet = False #toggle entire set loop
        elif (alphaPairsChanged == 0): entireSet = True  
        print "iteration number: %d" % iter
    return oS.b,oS.alphas
        
                
            
def calcWs(alphas,dataArr,classLabels):
    X=mat(dataArr)
    labelMat=mat(classLabels).transpose()
    m,n=shape(X)
    w=zeros((n,1))
    for i in range(m):
        w+=multiply(alphas[i]*labelMat[i],X[i,:].T)
    return w


#核函数转换
'''def kernelTrans(X,A,kTup):
    m,n=shape(X)
    K=mat(zeros((m,1)))
    if kTup[0]=='lin':
        K=X*A.T
    elif kTup[0]=='rbf':
        for j in range(m):
            deltaRow=X[j,:]-A
            K[j]=deltaRow*deltaRow.T
        K=exp(K/(-1*kTup[1]**2))
    else:
        raise NameError('Houston we have a problem--That Kernel is not recognized')
    return K

class optStruct:
    def __init__(self,dataMatIn,classLabels,C,toler,kTup):
        self.X=dataMatIn
        self.labelMat=classLabels
        self.C=C
        self.tol=toler
        self.m=shape(dataMatIn)[0]
        self.alphas=mat(zeros((self.m,1)))
        self.b=0
        self.eCache=mat(zeros((self.m,2)))
        self.K=mat(zeros((self.m,self.m)))
        for i in range(self.m):
            self.K[i,:]=kernelTrans(self.X,self.X[i,:],kTup)'''
            
def testRbf(k1=1.3):
    dataArr,labelArr=loadDataSet('testSetRBF.txt')
    b,alphas=smoP(dataArr,labelArr,200,0.0001,10000,('rbf',k1))
    datMat=mat(dataArr)
    labelMat=mat(labelArr).transpose()
    svInd=nonzero(alphas.A>0)[0]
    sVs=datMat[svInd]
    labelSV=labelMat[svInd]
    print "there are %d Support Vectors"%shape(sVs)[0]
    m,n=shape(datMat)
    errorCount=0
    for i in range(m):
        kernelEval=kernelTrans(sVs,datMat[i,:],('rbf',k1))
        predict=kernelEval.T*multiply(labelSV,alphas[svInd])+b
        if sign(predict)!=sign(labelArr[i]):
            errorCount+=1
    print "the training error rate is:%f"%(float(errorCount/m))
    dataArr,labelArr=loadDataSet('testSetRBF2.txt')
    errorCount=0
    datMat=mat(dataArr)
    labelMat=mat(labelArr).transpose()
    m,n=shape(datMat)
    for i in range(m):
        kernelEval=kernelTrans(sVs,datMat[i,:],('rbf',k1))
        predict=kernelEval.T*multiply(labelSV,alphas[svInd])+b
        if sign(predict)!=sign(labelArr[i]):
            errorCount+=1
    print "the training error rate is:%f"%(float(errorCount/m))
            
    
    
#基于SVM的手写数字识别
def loadImages(dirName):
    from os import listdir
    hwLabels=[]
    trainingFileList=listdir(dirName)
    m=len(trainingFileList)
    trainingMat=zeros((m,1024))
    for i in range(m):
        fileNameStr=trainingFileList[i]
        fileStr=fileNameStr.split('.')[0]
        classNumStr=int(fileStr.split('_')[0])
        if classNumStr==9:
            hwLabels.append(-1)
        else:
            hwLabels.append(1)
        trainingMat[i,:]=img2vector('%s/%s'%(dirName,fileNameStr))
    return trainingMat,hwLabels



def testDigits(kTup=('rbf',10)):
    dataArr,labelArr=loadImages('trainingDigits')
    b,alphas=smoP(dataArr,labelArr,200,0.0001,10000,kTup)
    datMat=mat(dataArr)
    labelMat=mat(labelArr).transpose()
    svInd=nonzero(alphas.A>0)[0]
    sVs=datMat[svInd]
    labelSV=labelMat[svInd]
    print "there are %d Support Vectors"%shape(sVs)[0]
    m,n=shape(datMat)
    errorCount=0
    for i in range(m):
        kernelEval=kernelTrans(sVs,datMat[i,:],('rbf',kTup))
        predict=kernelEval.T*multiply(labelSV,alphas[svInd])+b
        if sign(predict)!=sign(labelArr[i]):
            errorCount+=1
    print "the training error rate is:%f"%(float(errorCount/m))
    dataArr,labelArr=loadImages('testDigits')
    errorCount=0
    datMat=mat(dataArr)
    labelMat=mat(labelArr).transpose()
    m,n=shape(datMat)
    for i in range(m):
        kernelEval=kernelTrans(sVs,datMat[i,:],('rbf',kTup))
        predict=kernelEval.T*multiply(labelSV,alphas[svInd])+b
        if sign(predict)!=sign(labelArr[i]):
            errorCount+=1
    print "the training error rate is:%f"%(float(errorCount/m))
            
             
    
def img2vector(filename):
    returnVect = zeros((1,1024))
    fr = open(filename)
    for i in range(32):
        lineStr = fr.readline()
        for j in range(32):
            returnVect[0,32*i+j] = int(lineStr[j])
    return returnVect    
        
        
            
        
                   
                    
                
                
                
        
        
    
                    
                
                
                
                
                      
                      
    
    
    
    
    
    