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

#定制类
#__str__()返回用户看到的字符串
#__repr__()返回程序开发者看到的字符串，__repr__()是为调试服务的

class Animal(object):
    def __init__(self,color,kind):
        self.color = color
        self.kind = kind
    def __str__(self):
        return 'Animal object (color: %s, kind: %s)'%(self.color,self.kind)
    __repr__ = __str__

a = Animal('blue','bird')
print(a)

#类迭代 一个类被用于for循环，
# __iter__()方法，该方法返回一个迭代对象
#Python的for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值，
# 直到遇到StopIteration错误时退出循环
#__getitem__把一个用于for循环的类 当做list处理 通过index获取值
#斐波拉契数列
class Fib(object):
    def __init__(self):
        self.a,self.b = 0,1
    def __iter__(self):
        return self
    def __next__(self):
        self.a,self.b = self.b,self.a + self.b
        if self.a > 100:
            raise StopIteration()
        return self.a
    def __getitem__(self, n):
        a,b=1,1
        if isinstance(n,int):
            for index in range(n):#n 是索引
                a,b = b,a + b
            return a
        elif isinstance(n,slice):#n 是切片
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            if stop is None or stop < 0:
                raise  ValueError('error slice')
            a,b = 1,1
            L = []
            for index in range(stop):
                if index >= start:
                  L.append(a)
                a,b = b,a + b
            return L
        else:
            raise ValueError('error n')

def itFib():
    for n in Fib():
        print(n)
#itFib()
f = Fib()
print(f[0])
print(f[1])
print(f[3])
print(f[:10])

#__getattr__ 当调用不存在的属性时，
#比如score，Python解释器会试图调用__getattr__(self, 'score')来尝试获得属性
#一个对象实例可以有自己的属性和方法，当我们调用实例方法时，我们用instance.method()来调用
#__call__ 把实例看成一个函数
class Chain(object):
    def __init__(self,path = ''):
        self._path = path
    def __getattr__(self, path):
        return Chain('%s/%s'%(self._path,path))
    def __str__(self):
        return self._path
    __spec__ = __str__

    def __call__(self, *args, **kwargs):  # 使用实例不存在的方法时，会尝试用该函数解释
        print("called")
        return Chain("%s=%s" % (self._path, args))

print(Chain(), Chain()(), Chain()()())
print(Chain().status)
print(Chain().status.user("ksven"))
print(Chain().status.user("ksven").timeline)