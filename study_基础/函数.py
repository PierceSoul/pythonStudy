#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/3/16 上午10:23
# @File    : 函数.py
from functools import reduce
import functools

def addList(list):
    list.append([4,5,6])
    return list

list0 = [1,2,3]
addList(list0)

print(list0)
list1 = [1,2,3]
def fun(func,list):
    return func(list)
print(fun(addList,list1))

#可不指定顺序
def printInfo(name,age):
    print("name: ",name)
    print("age: ", age)
    return

printInfo(age = 24,name = "hehe")

#可变长参数
def changeArgs(*args):
    for var in args:
        print(var)

changeArgs(1,2,3)

#lambda表达式
sum = lambda arg1,arg2:arg1+arg2
print(sum(1,2))

#map()函数接收两个参数，一个是函数，一个是Iterable，
#map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。
def pow(n):
    return n * n
r = map(pow,[1,2,3,4,5])
print(list(r))
#reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，
# 这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，其效果就是：
#reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)

var = reduce(lambda x,y:x + y,[1,2,3,4,5])
print(var)

def str2int(s):
    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
    return reduce(lambda x,y:x*10+y,map(char2num,s))

print(str2int("12345") + 1)

#filter()也接收一个函数和一个序列。和map()不同的是，
# filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。
list2 = list(filter(lambda x:x%2 == 1,[1,2,3,4,5,6,7,8,9]))
print(list2)

#sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序
#字符串是根据ascii码排序
names = sorted(["bob","Alice","Slina","Zoo"],key = str.lower)
print(names)


L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):
    return t[0]. lower()
L2 = sorted(L, key=by_name)
print(L2)

#返回函数
def lazy_sum(*args):
    def sum():
        t = 0
        for n in args:
            t += n
        return t
    return sum

fsum = lazy_sum(1,2,3,4)
print(fsum())

#闭包
#注意：返回的函数并未执行 调用的时候才会执行

#返例 全部都是9！原因就在于返回的函数引用了变量i，但它并非立刻执行。
# 到3个函数都返回时，它们所引用的变量i已经变成了3，因此最终结果为9
def count():
    fs = []
    for i in range(1,4):
        def f():
            return i*i
        fs.append(f)
    return fs
list3 = count()
print(list3[0]())
print(list3[1]())
print(list3[2]())

def count1():
    fs = []
    for i in range(1,4):
        def f(j):
            return lambda : j*j
        fs.append(f(i))
    return fs
list4 = count1()
print(list4[0]())
print(list4[1]())
print(list4[2]())

#装饰器模式
#在执行方法时打印log
def log(text):
    def decorator(fun):
        def wrapper(*args,**kw):
            print("%s %s:"%(text,fun.__name__))
            return fun(*args,**kw)
        return wrapper
    return decorator

@log('execute')
def now():
    print("2017-7-16")
now()

#偏函数 固定函数某一个参数值 import functools
#转二进制
int2 = functools.partial(int,base=2)
int8 = functools.partial(int,base=8)
int16 = functools.partial(int,base=16)
print(int2('11000'))
print(int8('11000'))
print(int16('11000'))
