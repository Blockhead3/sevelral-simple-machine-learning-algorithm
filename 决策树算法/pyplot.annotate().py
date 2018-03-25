# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 17:22:20 2017

@author: Administrator
"""

'''matplotlib.pyplot.annotate(*args,**kwargs) 用文本s注解点xy,额外的kwargs传递给文本。'''
#s--字符串，注解的文本；xy--迭代器，长度2序列指定(x,y)点注释；xytext--迭代器，可选，长度2序列指定注解文本放置的位置。若值为None,默认在xy点。
#xycoords--字符串|可调用|元组，可选，给出xy的坐标系统，有一下值：1.'figure points'(从图中左下角的点);2.'figure pixels'(图中左下角的像素);3.'figure fraction'(左下角的比例|小部分)
       #4.'axes point'(来自子图左下角的点);5.'axes pixels'(子图左下角的像素);6.'axes fraction'(子图的左下角部分)；7.'data'(使用被注释的对象的坐标系统(默认));8.'polar'(极坐标)
#textcoords--字符串|可调用|元组，可选，给出了xytext的坐标系统，它可能与xy的坐标系不同。取值与xycoords一样。
#arrowprops--字典型，可选，如果取值不是None，属性用于在xy和xytext之间绘制一个箭头。当arrowprops不把话键arrowstyle,则用以下键：1.width(箭头的宽度);2.headwidth(箭头的底部的宽度);3.shrink(从两端到“缩小”的总长度的分数)
#annotation_clip--布尔，可选，控制在轴区域外注释的可见性


#例
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