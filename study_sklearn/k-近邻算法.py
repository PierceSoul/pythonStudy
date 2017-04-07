#!/usr/bin/env python
__author__ = 'Tony Liu'
# -*- coding: utf-8 -*-

from numpy import  *
import  operator

#准备数据集 用于算法学习
def createDataSet():
    group = array([[1.0,1],
                   [1.0,1.0],
                   [0,0],
                   [0,1]])
    labels = ['A','A','B','B']
    return group,labels

#K-近邻算法 (求两点最短距离) --分类算法
# (1)计算已知类别数据集中的点与当前点之间的距离；
# (2)按照距离递增次序排序；
# (3)选取与当前点距离最小的k个点
# (4)确定前k个点所在类别的出现频率；
# (5)返回前k个点出现频率最高的类别作为当前点的预测分类。
# shape方法：numpy提供 读取矩阵某个维度的长度
def classify0(inX,dataSet,labels,k):
    dataSetSize = dataSet.shape[0]
    # inX扩充成数据集的长度，每组数据都是一样的，然后计算各组与数据集的差值
    diffMat = tile(inX,(dataSetSize,1)) - dataSet
    # 得到的差值求平方
    sqDiffMat = diffMat**2
    # 将矩阵每一行相加 axis=1表示矩阵每一行所有数据相加 例：[[1,2],[3,4]] => [3,7]
    # axis=0 表示两个矩阵分别相加 例：[[1,2],[3,4]] => [4,6]
    sqDistances = sqDiffMat.sum(axis=1)
    # 开方
    distances = sqDistances**0.5
    #返回distances 升序排列的索引
    distancesIndex = distances.argsort()
    print(distancesIndex)
    # 选择距离最小的k个点。
    classCount = {}
    for i in range(k):
        voteIlabel = labels[distancesIndex[i]]
        #dict.get(k,default=None) 默认值
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
    print(classCount)
    sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)
    print(sortedClassCount)
    return sortedClassCount[0][0]


print(classify0([0,1],createDataSet()[0],createDataSet()[1],3))

