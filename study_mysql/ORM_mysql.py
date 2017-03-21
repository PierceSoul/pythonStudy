#!/usr/bin/env python
__author__ = 'Tony Liu'
# -*- coding: utf-8 -*-

from sqlalchemy import Column, Integer,String, create_engine,ForeignKey
from sqlalchemy.orm import sessionmaker,relationship
from sqlalchemy.ext.declarative import declarative_base


# 创建对象的基类:
Base = declarative_base()

class User(Base):
    # 表的名字:
    __tablename__ = 'user'

    # 表的结构:
    id = Column(Integer(), primary_key=True)
    name = Column(String(20))
    age = Column(Integer())
    gender = Column(Integer())
    books = relationship('Book')

class Book(Base):
    # 表的名字:
    __tablename__ = 'book'
    # 表的结构:
    id = Column(Integer(), primary_key=True)
    name = Column(String(20))
    # “多”的一方的book表是通过外键关联到user表的:
    user_id = Column(Integer(), ForeignKey('user.id'))

# 初始化数据库连接:
engine = create_engine('mysql+mysqlconnector://root:Sxb889961@localhost:3306/test')
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)

def insert():
    # 创建Session:
    session = DBSession()
    u = User(name='王麻子',age=48,gender=0)
    session.add(u)
    session.commit()
    session.close()
#insert()

def select():
    session = DBSession()
    us = session.query(User).all()
    for user in us:
        print(user.name,user.age,user.gender)
    # 关闭Session:
    session.close()
#select()
def selectForeign():
    session = DBSession()
    us = session.query(User).join(Book,isouter=True).all()
    print(us)
    for user in us:
        books = []
        for book in user.books:
            b = {'bid':book.id,'name':book.name}
            books.append(b)
        print(user.id,user.name,user.age,books)
    # 关闭Session:
    session.close()
selectForeign()