#!/usr/bin/env python
__author__ = 'Tony Liu'
# -*- coding: utf-8 -*-

#type() 不仅可以判断类型也能创建class 无需自己定义一个类
def fun(self,name = 'python'):
    print('hello %s'% name)
# 要创建一个class对象，type()函数依次传入3个参数：
# class的名称；
# 继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
# class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。

Hello = type('Hello',(object,),dict(hello = fun))
h = Hello()
h.hello()
print(type(Hello))
print(type(h))

# metaclass
# 除了使用type()动态创建类以外，要控制类的创建行为，还可以使用metaclass。
# 连接起来就是：先定义metaclass，就可以创建类，最后创建实例。
# 用处 ： 要编写一个ORM框架，所有的类都只能动态定义，
# 因为只有使用者才能根据表的结构定义出对应的类来。
class ListMetaclass(type):
    def __new__(cls, name, bases,attrs):
        attrs['add'] = lambda self,value:self.append(value)
        return type.__new__(cls,name,bases,attrs)
class MyList(list,metaclass=ListMetaclass):
    pass
l = MyList()
l.add(1)
print(l)









