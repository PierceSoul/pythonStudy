#!/usr/bin/env python
__author__ = 'Tony Liu'
# -*- coding: utf-8 -*-

#读取文件主要流程
def readFile():
    try:
        f = open('E:/gui-config.json', 'r')
        print(f.read())
    except FileNotFoundError as e:
        print('FileNotFoundError : %s' % e)
    finally:
        if f:
            f.close()
#readFile()

#使用with 关键字 省去关闭流的操作
def readFile2():
    try:
        with open('E:/gui-config.json', 'r') as f:
            print(f.read())
    except FileNotFoundError as e:
        print('FileNotFoundError : %s' % e)

#readFile2()

#逐行读取
def readFile3():
    try:
        with open('E:/gui-config.json', 'r') as f:
            for line in f.readlines():
                print(line)
    except FileNotFoundError as e:
        print('FileNotFoundError : %s' % e)
#readFile3()

#读二进制文件
def readFile4():
    try:
        with open('E:/1.jpg', 'rb',encoding='') as f:
            print(f.read())
    except FileNotFoundError as e:
        print('FileNotFoundError : %s' % e)
#readFile4()

#以某种编码方式读取文件
def readFile5():
    try:
        with open('E:/1.txt', 'r',encoding='gbk') as f:
            print(f.read())
    except FileNotFoundError as e:
        print('FileNotFoundError : %s' % e)
#readFile5()

#写文件
def writeFile1():
    try:
        with open('E:/1.txt', 'w',encoding='utf-8') as f:
            f.write('Hello\n')
            f.write('Python')
        readFile5()
    except FileNotFoundError as e:
        print('FileNotFoundError : %s' % e)
writeFile1()