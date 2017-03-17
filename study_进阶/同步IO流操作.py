#!/usr/bin/env python
__author__ = 'Tony Liu'
# -*- coding: utf-8 -*-

from io import StringIO
from io import BytesIO

#StringIO
def stringIOTest1():
   sio = StringIO()
   sio.write('hello\n')
   sio.write('world')
   print(sio.getvalue())
#stringIOTest1()

def stringIOTest2():
    sio = StringIO('Hello\nPython\nWorld')
    while (1):
        line = sio.readline()
        if line == '':
            break
        print(line)
#stringIOTest2()

#BytesIO
def bytesIOTest1():
    bio = BytesIO()
    bio.write("中文".encode('utf-8'))
    print(bio.getvalue())
#bytesIOTest1()
def bytesIOTest2():
    bio = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
    print(bio.read())
#bytesIOTest2()

