# -*- coding: utf-8 -*-
"""
Created on Thu Sep 07 15:30:22 2017

@author: Administrator
"""

'''datingDataMat,datingLabels=kNN.file2matrix('datingTestSet.txt')
import matplotlib  
import matplotlib.pyplot as plt  
fig=plt.figure()  
ax=fig.add_subplot(111)  
ax.scatter(datingDataMat[:,1],datingDataMat[:,2])  
    # 上句替换为：ax.scatter(datingDataMat[:,1],datingDataMat[:,2],15.0*array(datingLabels),15.0*array(datingLabels))   
plt.show()

normMat,ranges,minVals=kNN.autoNorm(datingDataMat)
kNN.datingClassTest()

kNN.classifyPerson()'''

import kNN
"""testVector=kNN.img2vector('testDigits/0_13.txt')
print testVector[0,0:31]
print testVector[0,32:63]"""
kNN.handwritingClassTest()