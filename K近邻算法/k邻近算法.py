# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 19:02:48 2017

@author: Administrator
"""
from numpy import * 
import operator

def createDataSet():
    group=array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels=['A','A','B','B']
    return group,;labels
    
from numpy import * 
import operator
from os import listdir

#K-邻近算法
def classify0(inX,dataSet,labels,k): # inX---输入向量，dataSet---训练样本集，labels---标签向量，k---最近邻居的数据
    dataSetSize = dataSet.shape[0] #shape是array的一个属性，返回矩阵array的各个维度大小，shape[0]是返回矩阵第一列数据的个数。
    #array的shape函数返回指定维度的大小，如dataset为n*m的矩阵,dataSet.shape[0]返回n，dataSet.shape[1]返回m
    #计算距离
    diffMat = tile(inX,(dataSetSize,1)) - dataSet # 求差（求出的结果也是一个矩阵）,tile()函数可以重复输入向量，组成一个与训练数据dataSet行数一样多的矩阵
    sqDiffMat = diffMat**2 #求平方（结果仍是矩阵；是给矩阵的每个元素平方）
    sqDistances = sqDiffMat.sum(axis=1)  #对平方求和（求出的结果是一个列向量），sum函数,axis=1，表示将[]里面数相加（行相加）,axis=0表示(列相加)，axis=None(行列相加)   
    distances = sqDistances**0.5 #开方，即所求欧氏距离。
    #排序
    sortedDistIndicies = distances.argsort()  #返回distances排序的索引，用于下面查找标签
    classCount={} #定义元字典（）
    #选择距离最近的k个点
    for i in range(k): #遍历前k个点
        voteIlabel=labels[sortedDistIndicies[i]] #获得前k个点的标签
        classCount[voteIlabel]=classCount.get(voteIlabel,0)+1 # 统计前k个点的标签分别出现的次数。dict.get(key,default=None) 对字典dict中的键key,返回它对应的值value，如果字典中不存在此键，则返回default 的值(注意，参数default 的默认值为None)
    #排序
    sortedClassCount=sorted(classCount.iteritems(),key=operator.itemgetter(1),reverse=turn)
    #sorted函数:返回一个经过排序的列表
    #classCount.iteritems()：返回一个迭代器
    #operator.itemgetter: operator模块提供的itemgetter函数用于获取对象的哪些维的数据，参数为一些序号（即需要获取的数据在对象中的序号），下面看例子。
    # #reverse:reverse：是一个布尔值。如果设置为True，列表元素将被降序排列，默认为升序排列。
    return sortedClassCount[0][0]  #返回个数最多的标签
    
 
#将文件内容转换成所需的矩阵格式   
def file2matrix(filename):
    fr=open(filename) #打开文件，获得文件内容
    arrayOLines=fr.readlines() #分行获取文件内容
    numberOfLines=len(arrayOLines) #获得文件的行数
    returnMat=zeros((numberOfLines,3)) #先用零元素创建需要返回的numpy矩阵，（行数，列数）
    classLabelVector=[] #创建空的标签列表
    index=0
    #循环处理文件中的每一行数据
    for line in arrayOLines:
        line=line.strip() #strip() 方法用于移除字符串头尾指定的字符（默认为空白符（包括'\n','\r','\t',' '），此处是截掉所有的回车字符
                          #使用tab字符\t将上一步得到的整行数据分割成一个元素列表
        listFormLine=line.split('\t') #str.split(str="", num=string.count(str)).split()通过指定分隔符对字符串进行切片，如果参数num 有指定值，则仅分隔 num 个子字符串,#参数:str -- 分隔符，默认为空格。num -- 分割次数。 '\t'代表一个tab字符  
        returnMat[index,:]=linstFormLine[0:3] #选取列表的前3个元素放入numpy矩阵中
        classLabelVector.append(int(listFormLines[-1])) #将列表的最后一列存储到向量classLabelVector中
        index += 1
    return returnMat,classLabelVector #返回数据集矩阵和对应的标签向量 


#归一化处理数据
def autoNorm(dataSet): #autoNorm()函数，可以自动将数字特征值转化为0到1的区间。输入参数是原始数据集
    minVals=dataSet.min(0) #求出数据集中的最小值，参数0：从每一列中获得最小值，从而minVals是一个行向量。
    maxVals=dataSet.max(0) #求出数据集中的最大值，参数0：从每一列中获得最大值，从而maxVals是一个行向量。
    ranges=maxVals-minVals #求出归一化数据范围,向量。
    normDataSet=zeros(shape(dataSet)) #定义空的要返回的归一化后的矩阵，该矩阵和输入的原始数据集是一样的大小 
    m=dataSet.shape[0] #m是原数据集的行数
    normDataSet=dataSet-tile(minVals,(m,1)) #数据集与最小值相减，minVals是一个行向量，元素个数与数据集每行个数一样，用tile函数将其制作成与原数据一样大小的矩阵。
    normDataSet=normDataSet/tile(ranges,(m,1)) #矩阵除法，得到归一化之后的值。但在numpy库中 ，矩阵除法需要使用函数linalg.solve(matA,matB).
    return normDataSet,ranges,minVals
    
    
#测试代码
def datingClassTest():
    hoRatio=0.10 #取出10%的数据作为测试样例
    datingDataMat,datingLabels=file2matrix('datingTestSet.txt') #将文件中的数据转换成矩阵的形式，提取标签向量
    normMat,ranges,minVals=autoNorm(datingDatMat)#归一化处理
    m=normMat.shape[0] #数据总条数
    numTestVecs=int(m*hoRatio) #用于测试的数据条数
    errorCount=0.0 #初始化错误个数为0
    for i in range(numTestVecs): #对测试的数据进行遍历
        classifierResult=classify0(normMat[i,:],normMat[numTestVecs:m,:], datingLabels[numTestVecs:m],3)#对数据进行分类
        #normMat[i,:]是测试样例，归一化处理后的第i行，
        #normMat[numTestVecs:m,:]是训练数据，其样例的数量为 m-numTestVecs
        # datingLabels[numTestVecs:m]训练样本的标签向量， numTestVecs到 m-1  个                     
        print "the classifier came back with :%d,the real answer is:%d" % (classifierResult,datingLabels[i])
        #给出分类结果和实际结果            
        if  (classifierResult!=datingLabels[i]): errorCount += 1.0 #如果分类结果和测试结果不一样，分类错误个数加 1
    print "the total error rate is:%f " %(errorCount/float(numTestVecs))        
    print errorCount 
     

#约会网站预测函数
def classifyPerson():
    resultList=['not at all','in small doses','in large doses']#定义分类结果的类别
    percentTats=float(raw_input("percentage of time spent playing video games?"))#读取输入数据
    ffMiles=float(raw_input("frequent flier miles earned per year?"))#读取输入数据
    iceCream=float(raw_input("liters of ice cream consumed per year?"))#读取输入数据
    datingDataMat,datingLabels=file2matrix('datingTestSet.txt')#从文件中读取已有数据
    normMat,ranges,minVals=autoNorm(datingDataMat)#归一化处理
    inArr=array([ffMiles,percentTats,iceCream])#将单个输入数据定义成一个数据（一条数据/样例）
    classifierResult=classify0((inArr-minVals)/ranges,normMat,datingLabels,3)#对数据进行分类
    print "You will probably like this person: ",resultList[classifierResult-1]#输出预测的分类结果
    
    
    
#手写识别实例
# 将图像格式转变成一个向量，以便分类器识别   
def img2vector(filename):
    returnVect=zeros((1,1024)) #创建 1×1024的numpy数组
    fr=open(filename)#打开文件
    for i in range(32):#循环读出文件的前32行
        lineStr=fr.readline() #.readline()每次只读取一行，而.readlines()自动将文件内容分析成一个行的列表；
        for j in range(32):#将每行的前32个字符值储存在numpy数组中(从0到31列)
            returnVect[0,32*i+j]=int(lineStr[j])#储存位置（0,32*i+j）:第一行，第32*i+j列
    return returnVect #返回 1×1024的矩阵
    
#手写识别系统的测试代码
def handwritingClassTest():
    hwLabels=[] #定义手写字符的标签（类别）
    trainingFileList=listdir('trainingDigits')#列出目录下所有文件
    m=len(trainingFileList)#计算训练文件的数目
    trainingMat=zeros((m,1024))#创建 m×1024 训练矩阵
    #从文件名中解析出分类数字
    for i in range(m):
        fileNameStr=trainingFileList[i] #获得文件名
        fileStr=fileNameStr.split('.')[0] #用"."分割文件名，选取第一个分片。例 分割字符串 9_87.txt，返回9_87
        classNumStr=int(fileStr.split('_')[0])#获取文件名的类标签：用"_"分割，选取第一个分片，例 分割9_87，返回 9
        hwLabels.append(classNumStr)#把类标签存储到hwLabels中
        trainingMat=[i,:]=img2vector('trainingDigits/%s'%fileNameStr)#把文件变成向量并赋值到trainingMat这个矩阵中 .%s:定义字符串，%fileNameStr：用fileNameStr替代s
    testFileList=listdir('testDigits')#列出测试目录下的所有文件
    errorCount=0.0 #给分类错误数赋初值为0
    mTest=len(testFileList)#计算测试文件的数目
    for i in range(mTest):
        fileNameStr=testFileList[i]#获取文件名
        fileStr=fileNameStr.split('.')[0]#分割字符串，选取第一分片
        classNumSrt=int(fileStr.split('_')[0])#获得类标签
        vectorUnderTest=img2vector('testDigits/%s'%fileNameStr)#把文件转换成向量
        classifierResult=classify0(vectorUnderTest,trainingMat,hwLabels,3)#对测试样例分类
        print "the classifier came back with:%d,the real answer is:%d"%(classifierResult,classNumstr)#输出预测结果与真实结果
        if (classifierResult!=classNumStr): 
            errorCount += 1.0 #如果二者不一致，分类错误数 +1
    print "\nthe total number of errors is:%d" % errorCount
    print "\nthe total error rate is:%d" % (errorCount/float(mTest)) 

        
        
        
        
    
    
    
    
    
    
    
    
        
        
        
        
            
            
    
    
    
    
    
    
    
    