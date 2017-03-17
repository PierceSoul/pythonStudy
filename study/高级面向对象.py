#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/3/16 下午11:18
# @File    : 高级面向对象.py

class Person(object):
    pass

#给实例绑定属性和方法 注意：只对当前实例有效 ，类创建的其他实例无效
p = Person()
p.name = 'Bob'
p.age = 17
print(p.name)
print(p.age)
from types import MethodType
def set_age(self,age):
    self.age = age
p.set_age = MethodType(set_age,p)
p.set_age(18)
print(p.age)

#给类绑定属性和方法
Person.age = 10
Person.set_age = set_age
p1 = Person()
print(p1.age)
p1.set_age(18)
print(p1.age)

#__slots__限制类属性的绑定 仅对当前类实例起作用，对继承的子类是不起作用的：
#除非在子类中也定义__slots__，这样，子类实例允许定义的属性就是自身的__slots__加上父类的__slots__。
class Animal(object):
    __slots__ = ('kind','run')
a = Animal()
a.kind = "Dog"

#@property 即可获取属性 又可设置属性 免去get set操作
class Student(object):
    @property #可读写
    def birth(self):
        return self._birth
    @birth.setter
    def birth(self,val):
        if not isinstance(val,int):
            raise ValueError('birth must be an integer!')
        elif val <= 0:
            raise ValueError('birth must > 0!')
        else:
            self._birth = val
    @property
    def age(self):
        return 2017 - self._birth

s = Student()
s.birth = 1993
print(s.birth)
print(s.age)





