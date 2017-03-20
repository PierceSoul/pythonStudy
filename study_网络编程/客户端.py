#!/usr/bin/env python
__author__ = 'Tony Liu'
# -*- coding: utf-8 -*-

import socket
def sinaTest():
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect(("www.sina.com.cn",80))
    s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')
    buffer = []
    while True:
        d = s.recv(1024)
        if d:
            buffer.append(d)
        else:
            break
    data = b''.join(buffer)
    s.close()
    header,html = data.split(b'\r\n\r\n', 1)
    print(header.decode('utf-8'))
    with open('C:/Users/Administrator/Desktop/sina.html','wb') as f:
        f.write(html)
#sinaTest()

def clientTcp():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 建立连接:
    s.connect(('127.0.0.1', 9999))
    # 接收欢迎消息:
    print(s.recv(1024).decode('utf-8'))
    for data in [b'Michael', b'Tracy', b'Sarah']:
        # 发送数据:
        s.send(data)
        print(s.recv(1024).decode('utf-8'))
    s.send(b'exit')
    s.close()
#clientTcp()

def clientUdp():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    for data in [b'Michael', b'Tracy', b'Sarah']:
        # 发送数据:
        s.sendto(data, ('127.0.0.1', 9998))
        # 接收数据:
        print(s.recv(1024).decode('utf-8'))
    s.close()
clientUdp()