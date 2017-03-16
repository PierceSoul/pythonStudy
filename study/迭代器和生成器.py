#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/3/16 上午10:07
# @File    : 迭代器和生成器.py
import sys


list = [1,2,3,4]
it = iter(list)
for num in range(len(list)):
    print(next(it))

#生成迭代器
def fibonacci(n):
    a,b,counter = 0,1,0
    while (1):
        if(counter > n):
            return
        yield a
        a,b = b,a + b
        counter += 1

f = fibonacci(10)

while (1):
    try:
        print (next(f), end=" ")
    except StopIteration:
        sys.exit()