#!/usr/bin/env python
__author__ = 'Tony Liu'
# -*- coding: utf-8 -*-

import socket
import threading
import time

def serverTcp():
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.bind(('127.0.0.1',9999))
    s.listen(5)
    print('Waiting for connection...')
    while True:
        sock,addr = s.accept()
        t = threading.Thread(target = tcpLink,args = (sock,addr))
        t.start()

def serverUdp():
    s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    s.bind(('127.0.0.1',9998))
    print('Waiting for connection...')
    while True:
        data, addr = s.recvfrom(1024)
        print("Received from %s:%s." % addr)
        s.sendto(b'Hello, %s!' % data, addr)

def tcpLink(sock,addr):
    print('Accept new connection from %s:%s...' % addr)
    sock.send(b'Welcome!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('Connection from %s:%s closed.' % addr)
#serverTcp()
serverUdp()

