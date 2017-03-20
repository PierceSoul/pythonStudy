#!/usr/bin/env python
__author__ = 'Tony Liu'
# -*- coding: utf-8 -*-

import pickle
import os
import json

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
#picklingTest()

#dict json序列化
dict = dict(name='Bob', age=20, score=88)
jd = json.dumps(dict)
print(jd)
dictj = json.loads(jd)
print(dictj)

#class json序列化
class Student(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def json2class(d):
        return Student(d['name'],d['age'])

s = Student("Bob",18)
sj = json.dumps(s,default=lambda obj:obj.__dict__)
print(sj)
js = json.loads(sj,object_hook=Student.json2class)
print(js.name)
