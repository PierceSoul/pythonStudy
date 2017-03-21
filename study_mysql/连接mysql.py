#!/usr/bin/env python
__author__ = 'Tony Liu'
# -*- coding: utf-8 -*-
import mysql.connector
config = {
    'host':'localhost',
    'user':'root',
    'password':'Sxb889961',
    'database':'test',
    'charset':'utf8'
}
try:
    conn = mysql.connector.connect(**config)
except mysql.connector.Error as e:
    print('connect fails!{}'.format(e))

def insert():
    param = ('李四',28,0)
    try:
        cursor = conn.cursor()
        sqlinsert = "insert into user(name,age,gender) values(%s,%s,%s)"
        cursor.execute(sqlinsert,param)
        conn.commit()
        cursor.close()
    except mysql.connector.Error as e:
        print('connect fails!{}'.format(e))
#insert()

def select():
    try:
        cursor = conn.cursor()
        sqlselect = "select id,name,age,gender from user"
        cursor.execute(sqlselect)
        values = cursor.fetchall()
        cursor.close()
        conn.close()
        print(values)
    except mysql.connector.Error as e:
        print('connect fails!{}'.format(e))
select()

def update():
    param = (38, 2)
    try:
        cursor = conn.cursor()
        sqlupdate= "update user set age=%s where id=%s"
        cursor.execute(sqlupdate,param)
        conn.commit()
        cursor.close()
    except mysql.connector.Error as e:
        print('connect fails!{}'.format(e))
#update()

def delete():
    param = (1,)
    try:
        cursor = conn.cursor()
        sqldelete= "delete from user where id=%s"
        cursor.execute(sqldelete,param)
        conn.commit()
        cursor.close()
    except mysql.connector.Error as e:
        print('connect fails!{}'.format(e))
#delete()