#!/usr/bin/env python
__author__ = 'Tony Liu'
# -*- coding: utf-8 -*-

#类似java的try catch finally 父类异常Exception
#python try except finally 父类异常BaseException
# 子类和父类异常类不能同时出现 永远不会由子类捕获异常 和java一样的
#示例
def exceptEx():
    try:
        r = 10 / int('0')
    except ZeroDivisionError as e:
        print("ZeroDivisionError: %s"% e)
    except ValueError as e:
        print("ValueError: %s" % e)
    else:
        print("no error")
    finally:
        print("finally...")

#exceptEx()

#调用堆栈信息
def foo(s):
    return 10 / int(s)
def bar(s):
    return foo(s) * 2
def main():
    bar('0')

#main()

#记录错误日志
import logging

def foo1(s):
    return 10 / int(s)

def bar1(s):
    return foo(s) * 2

def main1():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)

#main1()
print('END')
