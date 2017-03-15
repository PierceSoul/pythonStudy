import switch as switch
#coding:utf8

def calculate(op,a,b):
   if "+" == op :
       add(a, b)
   elif "-" == op :
       cut(a, b)


def add(a,b):
    return print(a + b)
def cut(a,b):
    return print(a - b)


def f(x):
    print(x)

f({'a':1,'b':2})

def f(x,y):
    print("%d : %d_" % (x,y) *20)
f(1,2)

g = lambda x,y:x*y
print(g(2,3))
