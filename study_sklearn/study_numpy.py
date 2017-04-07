#!/usr/bin/env python
__author__ = 'Tony Liu'
# -*- coding: utf-8 -*-

from numpy import *

arr = random.rand(4,4)
print(arr)
#转化成4*4矩阵
matrixFromArr = mat(random.rand(4,4))
print(matrixFromArr)
#转置矩阵
matrixFromArrTran = matrixFromArr.T
print(matrixFromArrTran)
#矩阵求逆
matrixFromArrConver = matrixFromArr.I
print(matrixFromArrConver)
#matrixFromArr*matrixFromArrConver = I
I = matrixFromArr * matrixFromArrConver
print(I)
