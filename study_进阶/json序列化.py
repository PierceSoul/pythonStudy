#!/usr/bin/env python
__author__ = 'Tony Liu'
# -*- coding: utf-8 -*-

import pickle
import os

#pickling java中叫serializable

basePath = r'F:\pythontemp'

def picklingTest():
    d = dict(name='Bob', age=20, score=88)
    print(d)
    filePath = basePath + r"\dump.txt"
    #if not os.path.exists(filePath):
    #    os.mknod(filePath)
    #序列化成文件
    with open(filePath,"wb") as f:
        pickle.dump(d,f)
    #从文件反序列化
    with open(filePath, "rb") as f1:
        d = pickle.load(f1)
    print(d)
    os.remove(filePath)
picklingTest()