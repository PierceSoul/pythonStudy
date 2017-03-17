#!/usr/bin/env python
__author__ = 'Tony Liu'
# -*- coding: utf-8 -*-

import os

#获取操作系统
#posix，说明系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统
def getOs():
    print(os.name)
#getOs()

#os.uname() 要获取详细的系统信息，可以调用uname()函数：Windows上不提供

#获取操作系统的环境变量 dict结构
def getEnvValue():
    dict = os.environ
    print(dict)
    print(dict['FP_NO_HOST_CHECK'])
#getEnvValue()

#文件与目录操作
def dirAndFileTest():
    basePath = 'F:\pythontemp'
    print("当前目录的绝对路径：os.path.abspath('.')")
    src = os.path.abspath('.')
    print(src)
    print("在某个目录下创建一个新目录:os.path.join(basePath, 'testdir') ")
    retPath = os.path.join(basePath, 'testdir')
    print(retPath)
    print("然后创建一个目录: os.mkdir(path)")
    os.mkdir(basePath+'/test1')
    os.mkdir(basePath + '/test2')
    print("删除一个目录: os.rmdir(path)")
    os.rmdir(basePath + '/test2')
    l =  [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']
    print(l)
dirAndFileTest()
