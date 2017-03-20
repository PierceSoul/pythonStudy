#!/usr/bin/env python
__author__ = 'Tony Liu'
# -*- coding: utf-8 -*-

import random, time, queue
from multiprocessing.managers import BaseManager

class QueueManager(BaseManager):
    pass


def test():

    QueueManager.register('get_task_queue')
    QueueManager.register('get_result_queue')

    server_addr = '127.0.0.1'
    print('Connect to server %s ...' % server_addr)
    m = QueueManager(address = (server_addr, 5000), authkey = b'abc')

    reconnect = 5
    cnt = 0
    ok = False
    while cnt < reconnect:
        try:
            m.connect()
        except:
            print('server not ready...')
            time.sleep(5)
        else:
            ok = True
            break
        cnt += 1

    if not ok:
        return None


    task = m.get_task_queue()
    result = m.get_result_queue()

    for i in range(10):
        #从任务队列里取一个任务
        try:
            n = task.get(timeout = 1)
            r = '%d * %d = %d ' % (n, n, n * n)
            print('Put result %s to queue...' % r)
            result.put(r)
            time.sleep(1)
        except queue.Empty:
            print('task queue is empty')

    print('worker exit.')


if __name__ == '__main__':
    #freeze_support()
    test()
