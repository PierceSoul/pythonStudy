#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
import codecs
from multiprocessing import Pool
import requests
import sqlite3
from .conf import db_name
from bs4 import BeautifulSoup

connect = sqlite3.connect(db_name)
cursor = connect.cursor()

# 创建表
cursor.execute('''CREATE TABLE IF NOT EXISTS cheHang168User
(id varchar(20), phone integer(20), username varchar(20))
''')

# 数据库存的用户ID
user_ids = cursor.execute("SELECT id FROM cheHang168User").fetchall()

cursor.close()
connect.commit()
connect.close()


url = "http://m.chehang168.com/u/jqmno_"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6',
    'X-Forwarded-For': '511.1.1.1, 512.2.2.2, 513.3.3.3',
    'X-Real-IP': '512.1.1.0'
}

def Spider(page):

    if (str(page),) in user_ids:
        print("数据库存在 " + str(page))
        return

    tempurl = url + str(page) + '/zylist.html'

    s = requests.session()
    s.headers.update(headers)
    result = s.get(tempurl)
    if result.ok:
        soup = BeautifulSoup(result.content, "html.parser")

        user_name = soup.find_all('h2')
        if len(user_name) > 0:
            user_name = user_name[0].text
        else:
            print("人名不存在 " + tempurl)
            return

        if user_name == u" (更新：) ":
            print("人名不存在 " + tempurl)
            return

        user_phone = soup.find_all('a')
        if len(user_name) > 0:
            user_phone = user_phone[0].text
        else:
            print('电话不存在 ' + tempurl)
            return

        conection = sqlite3.connect(db_name, timeout=30.0)
        cursor = conection.cursor()
        cursor.execute(
            "INSERT INTO cheHang168User (id, phone, username) VALUES (?, ?, ?);",
            (page, user_phone, user_name,))
        cursor.close()
        conection.commit()
        conection.close()
        print(tempurl)
    else:
        print("请求失败 " + tempurl)
        exit()


def find_max_page():

    base_page = 163000
    add_count = 1000
    print("查找最大 用户ID.....")
    while 1:
        tempurl = url + str(int(base_page + add_count)) + '/zylist.htm'
        result = requests.get(tempurl)
        print(tempurl)
        if result.ok:
            soup = BeautifulSoup(result.content, "html.parser")
            soup.find_all()

            user_name = soup.find_all('h2')
            if len(user_name) > 0:
                user_name = user_name[0].text
            else:
                print("人名不存在 " + tempurl)

            if (user_name == u" (更新：) ") or (len(user_name) == 0):
                # print('if 无' + str(base_page))
                add_count = int(add_count / 2)
                base_page = base_page - add_count

                if add_count < 2:
                    print("最大用户ID " +  + tempurl)
                    break
            else:
                # print('else 有' + str(base_page))
                base_page = base_page + add_count
        else :
            print("链接错误" + tempurl)
            exit()

    return 0

# find_max_page()

begin_page = int(input(u'请输入开始的页数：\n'))
end_page = int(input(u'请输入终点的页数：\n'))

Pool().map(Spider, range(begin_page, end_page+1))

print('done')