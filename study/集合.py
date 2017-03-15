#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/3/15 下午11:24
# @File    : 集合.py

#列表List
list1 = ['c','a','b']
list2 = ['d','e']
list3 = list1  + list2
print( 'b' in list3)
print( list3 * 2)
print( max(list1))

#元组 元组使用小括号，列表使用方括号。
tup1 = (1,2,3,4)
tup2 = (5,6)
tup3 = tup1 + tup2

#元组只包含一个元素时要添加逗号
tup4 = (7,)
del tup4
#print(tup4)

# 列表转换元组
tup5 = tuple(list3)
print(tup5)
#元组转换列表
list4 = list(tup3)
print(list4)

#字典 值可以取任何数据类型，但键必须是不可变的，如字符串，数字或元组。
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