# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 14:20:31 2017

@author: cabbage
"""


from numpy import *


#词表到向量的转换函数
def loadDataSet():
    postingList=[['my','dog','has','flea','problems','help','please'],
                 ['maybe','not','take','him','to','dog','park','stupid'],
                 ['my','dalmation','is','so','cute','I','love','him'],
                 ['stop','posting','stupid','worthless','garbage'],
                 ['mr','likes','ate','my','steak','how','to','stop','him'],
                 ['quit','buying','worthless','dog','food','stupid']] #进行词条分割后的文档集合。
    classVec=[0,1,0,1,0,1] #类别标签，1:代表侮辱性文字，0：正常言论
    return postingList,classVec
    
def createVocabList(dataSet): #创建包含所有文档中出现的不重复词的列表
    vocabSet=set([]) #创建空集，set数据类型
    for document in dataSet:
        vocabSet=vocabSet|set(document) #操作符"|"是求两个集合的并集，将每篇文档返回的新词汇添加到该集合。
    return list(vocabSet)
    
def setOfWords2Vec(vocabList,inputSet):#输入参数：词汇表、某个文档。输出：数字向量
    returnVec=[0]*len(vocabList)#创建一个与词汇表等长的向量，将其元素都设置为0
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)]=1 #若出现了词汇表中单词，则将输出文档向量中对应的值设置为1
        else: print "the word :%s is not in my Vocabulary!" % word
    return returnVec    
    

#朴素贝叶斯分类器训练函数（此处就1类和0类）
def trainNB0(trainMatrix,trainCategory):#trainMatrix:文档矩阵；trainCategory:由每篇文档类别标签构成的向量
    numTrainDocs=len(trainMatrix) #计算trainMatrix的行数
    numWords=len(trainMatrix[0]) #计算trainMatrix的列数
    pAbusive=sum(trainCategory)/float(numTrainDocs)#文档属于分类1的概率
    p0Num=ones(numWords) #属于类别0的词向量求和
    p1Num=ones(numWords)#属于类别1的词向量求和
    p0Denom=2.0 #类别0的所有文档内的单词求和
    p1Denom=2.0 #类别1的所有文档内的单词求和
    for i in range(numTrainDocs):
        if trainCategory[i]==1: #若文档属于类别1
            p1Num += trainMatrix[i] #属于类1的词向量累加（向量列表）
            p1Denom += sum(trainMatrix[i]) #类别1文档单词数累加（在类1中，出现的单词总个数）
        else:
            p0Num += trainMatrix[i]
            p0Denom += sum(trainMatrix[i])
    p1Vect=log(p1Num/p1Denom)  #各单词在类别1条件下出现的频数取对数(对每个元素做除法)向量列表
    p0Vect=log(p0Num/p0Denom)  #各单词在类别0条件下出现的频数取对数（向量列表）
    return p0Vect,p1Vect,pAbusive
            

#朴素贝叶斯分分类函数
def classifyNB(vec2Classify,p0Vec,p1Vec,pClass1): #vec2Classify:要分类的向量(数字向量);p0Vec|p1Vec:各单词在类别0|1条件下出现的概率;pClass1:文档属于类1的概率
    p1 = sum(vec2Classify * p1Vec) + log(pClass1)#此形式是对数的缘故
    p0 = sum(vec2Classify*p0Vec) + log(1.0 - pClass1)
    if p1 > p0:
        return 1
    else:
        return 0
        
def testingNB():
    listOPosts,listClasses=loadDataSet() #listOposts:进行词条切分后的文档(文档是列表)集合；listClasses:类别标签集合
    myVocabList=createVocabList(listOPosts) #myVocabList:词汇表（所有listOposts中出现的不重复的单词）
    trainMat=[] #存储将文档列表转化成数字列表的列表
    for postinDoc in listOPosts:
        trainMat.append(setOfWords2Vec(myVocabList,postinDoc)) #调用setOfWords2Vec（将postinDoc转化成数字向量列表）
    p0V,p1V,pAb = trainNB0(array(trainMat),array(listClasses)) #调用trainNB0函数
    testEntry= ['love','my','dalmation']
    thisDoc = array(setOfWords2Vec(myVocabList,testEntry))#转化成数字列表
    print testEntry,'classified as:',classifyNB(thisDoc,p0V,p1V,pAb) #调用classifyNB（），输出测试结果
    testEntry=['stupid','garbage']
    thisDoc=array(setOfWords2Vec(myVocabList,testEntry))
    print testEntry,'classified as:',classifyNB(thisDoc,p0V,p1V,pAb)
    
#朴素贝叶斯词袋模型
def bagOfWords2VecMN(vocabList,inputSet): #vocabList:词汇表(list)
    returnVec=[0]*len(vocabList)
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)]+=1
    return returnVec

#文本解析及完整的垃圾邮件测试函数
def textParse(bigString):
    import re
    listOfTokens=re.split(r'\W*',bigString)#用正则表达式切分句子,\W:匹配非数字、字母、下划线中的任意字符
    return [tok.lower() for tok in listOfTokens if len(tok)>2] #.lower():将字符串换成小写，返回长度>2的字符串
    
    
def spamTest():#解析文件成词列表
    docList=[]
    classList=[]
    fullText=[]
    for i in range(1,26):
        wordList=textParse(open('email/spam/%d.txt'% i).read())#打开spam中第i个文本,并分割
        docList.append(wordList)#储存切分后文本,每个元素（文本）是列表，总体是列表
        fullText.extend(wordList)#得到所以所以文本组成的一个列表
        classList.append(1)
        wordList=textParse(open('email/ham/%d.txt'% i).read())#打开ham中第i个文本,并分割
        docList.append(wordList)#储存切分后文本,每个元素（文本）是列表，总体是列表
        fullText.extend(wordList)#得到所以所以文本组成的一个列表
        classList.append(0)
    vocabList=createVocabList(docList)#词汇表
    trainingSet=range(50)#整数集，从0到49
    testSet=[]
    for i in range(10):#随机选取10个文件
        randIndex=int(random.uniform(0,len(trainingSet)))#产生一个0--len(trainingSet)之间的数
        testSet.append(trainingSet[randIndex]) #构建测试数据
        del(trainingSet[randIndex])#从训练集中删除
    trainMat=[]
    trainClasses=[]
    for docIndex in trainingSet: #基于词汇表，对每个邮件（文件），使用setOfWords2Vec()函数构建词向量
        trainMat.append(setOfWords2Vec(vocabList,docList[docIndex]))#调用setOfWords2Vec()函数，构建数字词向量（list）
        trainClasses.append(classList[docIndex])
    p0V,p1V,pSpam=trainNB0(array(trainMat),array(trainClasses))#调用trainNB0()计算分类所需概率
    errorCount=0 #初始误差为0
    for docIndex in testSet:#对测试集分类
        wordVector=setOfWords2Vec(vocabList,docList[docIndex])
        if classifyNB(array(wordVector),p0V,p1V,pSpam)!=classList[docIndex]:
            errorCount+=1
    print 'the error rate is:',float(errorCount/len(testSet))
    

#  RSS源分类器及高频词去除函数  
def calcMostFreq(vocabList,fullText):
    import operator
    freqDict={}
    for token in vocabList:
        freqDict[token]=fullText.count(token)#count():返回token在fullText中出现次数
    sortedFreq=sorted(freqDict.iteritems(),key=operator.itemgetter(1),\
                      reverse=True) #sorted():返回一个经过排序的列表,reverse=True:按降序排列，operator.itemgetter(1):获取第一个域的值
    return sortedFreq[:30]#返回排序最高的30个单词

def localWords(feed1,feed0):#feed1和feed0两个RSS源
    import feedparser
    docList=[]
    classList=[]
    fullText=[]
    minLen=min(len(feed1['entries']),len(feed0['entries']))
    for i in range(minLen):
        wordList=textParse(feed1['entries'][i]['summary'])#每次访问一条RSS源
        docList.append(wordList)
        fullText.extend(wordList)
        classList.append(1)
        wordList=textParse(feed0['entries'][i]['summary'])#每次访问一条RSS源
        docList.append(wordList)
        fullText.extend(wordList)
        classList.append(0)
    vocabList=createVocabList(docList)#转换成词向量
    top30Words=calcMostFreq(vocabList,fullText)#调用calcMostFreq()函数，选出排序最高的30个单词
    for pairW in top30Words:
        if pairW[0] in vocabList:
            vocabList.remove(pairW[0])#移除
    trainingSet=range(2*minLen)
    testSet=[]
    for i in range(20):
        randIndex=int(random.uniform(0,len(trainingSet)))
        testSet.append(trainingSet[randIndex])#从训练集选取测试集
        del(trainingSet[randIndex])#删除
    trainMat=[]
    trainClasses=[]
    for docIndex in trainingSet:
        trainMat.append(bagOfWords2VecMN(vocabList,docList[docIndex]))
        trainClasses.append(classList[docIndex])
    p0V,p1V,pSpam=trainNB0(array(trainMat),array(trainClasses))
    errorCount=0
    for docIndex in testSet:
        wordVector=bagOfWords2VecMN(vocabList,docList[docIndex])
        if classifyNB(array(wordVector),p0V,p1V,pSpam) != classList[docIndex]:
            errorCount += 1
    print 'the error rate is:',float(errorCount)/len(testSet)
    return vocabList,p0V,p1V
    
    
def getTopWords(ny,sf):
    import operator
    vocabList,p0V,p1V=localWords(ny,sf)
    topNY=[]
    topSF=[]
    for i in range(len(p0V)):
        if p0V[i] > -0.6:
            topSF.append((vocabList[i],p0V[i]))
        if p1V[i] > -0.6:
            topNY.append((vocabList[i],p1V[i]))
    sortedSF=sorted(topSF,key=lambda pair:pair[1],reverse=True)
    print "SF**SF**SF**SF**SF**SF**SF**SF**SF**SF**SF**SF**SF**"
    for item in sortedSF:
        print item[0]
    sortedNY=sorted(topNY,key=lambda pair:pair[1],reverse=True)
    print "NY**NY**NY**NY**NY**NY**NY**NY**NY**NY**NY**NY**NY**"
    for item in sortedNY:
        print item[0]
    



           
    