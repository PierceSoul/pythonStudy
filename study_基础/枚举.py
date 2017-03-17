#!/usr/bin/env python
__author__ = 'Tony Liu'
# -*- coding: utf-8 -*-

from enum import Enum, unique

Week = Enum('Week',('Mon','Tue','Wed','Thu','Fri','Sat','Sun'))

def itWeek():
    for name,member in Week.__members__.items():
        print(name, '=>', member, ',', member.value)
print(Week(2))

@unique
class Weekday(Enum):
    Sun = 0  # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

print(Weekday(0))

