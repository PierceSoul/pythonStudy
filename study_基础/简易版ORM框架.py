#!/usr/bin/env python
__author__ = 'Tony Liu'
# -*- coding: utf-8 -*-

#使用metaclass写一个ORM
#1，首先来定义Field类，它负责保存数据库表的字段名和字段类型
class Field(object):
    def __init__(self,name,column_type):
        self.name = name
        self.column_type = column_type
    def __str__(self):
        return '<%s:%s>'%(self.__class__.__name__,self.name)
#2，定义各个类型的field
class StringField(Field):
    def __init__(self,name):
        super(StringField,self).__init__(name,'varchar(128)')
class IntegerField(Field):
    def __init__(self,name):
        super(IntegerField, self).__init__(name,'bigint')
#3，编写ModelMetaclass
class ModelMetaclass(type):
    def __new__(cls,name,bases,attrs):
        if name == 'Model':
            return type.__new__(cls,name,bases,attrs)
        print('Found Model:%s'% name)
        mapping = dict()
        for k,v in attrs.items():
            if isinstance(v,Field):
                print('found mapping : %s ==> %s' % (k,v))
                mapping[k] = v
        for k in mapping.keys():
            attrs.pop(k)
        attrs['__mapping__'] = mapping
        attrs['__table__'] = name
        return type.__new__(cls, name, bases, attrs)
#4 编写Model 实现crud
class Model(dict,metaclass = ModelMetaclass):
    def __init__(self,**kw):
        super(Model, self).__init__(**kw)
    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise  AttributeError(r"'Model' object has no attribute '%s'" % key)
    def __setattr__(self, key, value):
        self[key] = value
    def save(self):
        fields = []
        params = []
        args = []
        for k,v in self.__mapping__.items():
            fields.append(v.name)
            params.append("?")
            args.append(getattr(self,k,None))
        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))
        print('SQL: %s' % sql)
        print('ARGS: %s' % str(args))

#5，测试
class User(Model):
    name = StringField('name')
    age = IntegerField('age')
    gender = IntegerField('gender_type')

u = User(name='张山',age = 19 ,gender = 0)
u.save()



