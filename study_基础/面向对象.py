#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/3/16 下午10:21
# @File    : 面向对象.py

import types

# 双下划线开头的实例变量是不是一定不能从外部访问呢？
# 其实也不是。不能直接访问__name是因为Python解释器对外把__name变量改成了_Student__name，
# 所以，仍然可以通过_Student__name来访问__name变量
class Person(object):
    def __init__(self, name, age, gender):
        self.__name = name
        self.__age = age
        self.__gender = gender

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_gender(self):
        return self.__gender

    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        self.__age = age

    def set_gender(self, gender):
        self.__gender = gender

    def print_person(self):
        print('%s: %s: %s' % (self.__name, self.__age, self.__gender))


p = Person('张三', 18, 'male')
p.print_person()
#判断一个变量是否是某个类型
print(isinstance(p, Person))

#继承和多态
class Animal(object):
    def run(self):
        print("Animal is running...")
class Dog(Animal):
    def run(self):
        print("Dog is running...")
class Pig(Animal):
    def run(self):
        print("Pig is running...")
def run_twice(animal):
    animal.run()
    animal.run()
run_twice(Animal())
run_twice(Dog())
run_twice(Pig())

#判断对象类型 class类型用isinstance
print(type(run_twice) == types.FunctionType)
print(type(123) == int)
a = Animal()
d = Dog()
print(isinstance(a , Animal))
print(isinstance(d , Animal))

#判断是哪种类型中的一种
print(isinstance([1, 2, 3], (list, tuple)))

#获取对象的所有属性和方法
print(dir("a"))
#getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状态
print(hasattr(d,'run'))

#实例属性和类属性 注意 ： 实例属性和类属性命名相同 则实例属性会覆盖类属性
class Ball(object):
    name = 'basketball'#实例属性
    def __init__(self,color):
        self.color = color #类属性

