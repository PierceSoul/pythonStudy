#!/usr/bin/env python
__author__ = 'Tony Liu'
# -*- coding: utf-8 -*-

from multiprocessing import Process,Pool,Queue
import os,time,random,subprocess

#multiprocessing 跨平台版本的多进程模块

def run_proc(name):
    print("run child process %s:%s"%(name,os.getpid()))

#启动子进程
'''
if __name__ == "__main__":
    print("parant process start %s " % os.getpid())
    p = Process(target = run_proc,args = ('tset',))
    print("child process start")
    p.start()
    p.join()#等待该进程运行结束
    print("child process end")
'''

#进程池
def long_time_task(name):
    print("run task %s:%s"%(name,os.getpid()))
    start = time.time()
    time.sleep(random.random() * 4)
    end = time.time()
    print("task %s runs %0.2f seconds"%(name,(end - start)))
'''
if __name__ == "__main__":
    print("parant process %s" % os.getpid())
    p = Pool(4)
    for i in range(5):
        p.apply_async(long_time_task,args = (i,))
    print("waiting for all subprocess done")
    p.close()
    p.join()
    print("all subprocess done")
'''

#运行行命令
'''
if __name__ == "__main__":
    print("$ ping www.baidu.com")
    r = subprocess.call(['ping','www.baidu.com'])
    print("exit code:",r)
'''

def write(q):
    for i in [1,2,3]:
        print("write process %s put val %s to queue" % (os.getpid(),i))
        q.put(i)
        time.sleep(random.random() * 5)

def read(q):
    while True:
        print("read process %s read val %s from queue" % (os.getpid(),q.get(True)))


#进程间通信 通过Queue实现
if __name__ == "__main__":
    q = Queue()
    pw = Process(target=write,args=(q,))
    pr1 = Process(target=read,args=(q,))
    pr2 = Process(target=read,args=(q,))
    pw.start()
    pr1.start()
    pr2.start()
    pw.join()
    pr1.terminate()
    pr2.terminate()

