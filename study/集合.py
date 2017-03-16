#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/3/15 下午11:24
# @File    : 集合.py
from collections import deque


#列表List
list1 = ['c','a','b']
list2 = ['d','e']
list3 = list1  + list2
print( 'b' in list3)
print( list3 * 2)
print( max(list1))
print("--------------遍历获取索引和值---------------")
def ergodicList(list):
    for i,v in enumerate(list):
        print(i,v)
ergodicList(list1)
#列表当成堆栈
print("--------------列表当成堆栈---------------")
stack = []
stack.append(1)
stack.append(2)
stack.append(3)
stack.append(4)
print(stack)
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())

# 列表当队列使用 但是拿列表用作这样的目的效率不高。
# 在列表的最后添加或者弹出元素速度快，然而在列表里插入或者从头部弹出速度却不快（因为所有其他的元素都得一个一个地移动）。
print("--------------列表当队列使用---------------")
queue = []
queue.append("a")
queue.append("b")
queue.append("c")
queue.append("d")
queue = deque(queue)
print(queue)
print(queue.popleft())
print(queue.popleft())
print(queue.popleft())
print(queue.popleft())

print("--------------列表推导式---------------")
#列表推导式
vec = [1,2,3]
listvec = [[3*x,2*x] for x in vec]
print(listvec)

print("--------------转置矩阵---------------")
matrix = [
    [1,2],
    [3,4],
    [5,6]
]
print("原矩阵matrix：",matrix)
print("--------------第一种转置方法---------------")
dematrix = [[row[i] for row in matrix]for i in range(2)]
print("转置matrix：",dematrix)
#第二种转置方法
print("--------------第二种转置方法---------------")
temp = []
for i in range(2):
    temp_row = []
    for row in matrix:
        temp_row.append(row[i])
    temp.append(temp_row)
print("转置matrix：",temp)

print("--------------元组---------------")
#元组 元组使用小括号，列表使用方括号。
tup1 = (1,2,3,4)
tup2 = (5,6)
tup3 = tup1 + tup2

#元组只包含一个元素时要添加逗号
tup4 = (7,)
del tup4
#print(tup4)

# 列表转换元组
print("--------------列表转换元组---------------")
tup5 = tuple(list3)
print(tup5)
#元组转换列表
print("--------------元组转换列表---------------")
list4 = list(tup3)
print(list4)

#字典 值可以取任何数据类型，但键必须是不可变的，如字符串，数字或元组。
print("--------------字典---------------")
dict = {"name":"liuTong","age":24}
print(dict['name'])
#删除key
del dict['name']
#清空
dict.clear()
print(dict)
#key值相同 后面的值会覆盖前面的值
dict1 = {"name": 'Zara', "age": 7, 'name': 'Manni'}
print(dict1)
print("--------------字典遍历---------------")
def ergodicDict(dict):
    for k,v in dict.items():
        print(k,v)
ergodicDict(dict1)