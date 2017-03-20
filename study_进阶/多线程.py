#!/usr/bin/env python
__author__ = 'Tony Liu'
# -*- coding: utf-8 -*-

import time, threading

#_thread和threading，_thread是低级模块，threading是高级模块，对_thread进行了封装。
# 绝大多数情况下，我们只需要使用threading这个高级模块

def loop():
    print("thread %s is running..." % threading.current_thread().name)
    n = 0
    while n < 5:
        n += 1
        print("thread %s >>> %s" % (threading.current_thread().name,n))
        time.sleep(1)
    print("thread %s end..." % threading.current_thread().name)

def runThread():
    print("thread %s is running..." % threading.current_thread().name)
    t = threading.Thread(target=loop,name = 'LoopThread')
    t.start()
    t.join()
    print("thread %s end..." % threading.current_thread().name)
#runThread()

balance = 0
lock = threading.Lock()
def change_balance(n):
    global balance
    balance += n
    balance -= n

def run_thread(n):
    for i in range(100000):
        #加锁
        lock.acquire()
        try:
            change_balance(n)
        finally:
            lock.release()



def testMutiThread():
    t1 = threading.Thread(target=run_thread,args=(5,))
    t2 = threading.Thread(target=run_thread, args=(8,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(balance)
#testMutiThread()

#ThreadLocal的使用
thread_local = threading.local()
def process_student():
    std = thread_local.student
    print("Hello,%s (in %s)" % (std,threading.current_thread().name))
def process_thread(name):
    thread_local.student = name
    process_student()

def threadLocalTest():
    t1 = threading.Thread(target=process_thread,args=("Bob",))
    t2 = threading.Thread(target=process_thread, args=("Alice",))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
threadLocalTest()