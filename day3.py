#递归算阶乘
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)
print(factorial(10))

#尾递归
def fact(n):
    return fact_iter(n,1)
def fact_iter(num,con):
    if num == 1:
        return con
    return fact_iter(num - 1,num * con)
print(fact(5))

createList = []
n = 1
while n <= 99:
    createList.append(n)
    n = n + 2
print(createList)

#切片
cutList = [1,2,3,4,5,6,7,8,9]
cutedList1 = cutList[1:3]
print(cutedList1)

#取倒数
cutedList2 = cutList[-1:]
print(cutedList2)

map = {"a":1,"b":2,"c":3}
for key in map :
    print(map.get(key))
l = [(1,1),(2,2),(3,3)]
for x,y in l :
    print(x,y)

#奇葩的循环表达式
ll = [""+str(x)+"*"+str(x)+"" for x in range(10)]
print(ll)
#奇葩的循环表达式加循环条件
#筛选出偶数
lll = [x * x for x in range(10) if x % 2 == 0]
print(lll)
#奇葩的两层循环表达式
llll = [ m + n  for m in "ABC" for n in "ABC" ]
print(llll)

#同时遍历map的key，value
