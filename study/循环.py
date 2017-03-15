# -*- coding: UTF-8 -*-
#循环及if
#while
numbers = [1,2,3,4,5,6,7,8,9,10]
even = []
odd = []
while (len(numbers) > 0):
    num = numbers.pop()
    if(num % 2 == 0):
        even.append(num)
    else:
        odd.append(num)
else:
    print("循环的else语句")
print("偶数集合  " + str(even))
print("奇数集合 " + str(odd)[1 : len(str(odd))-1])



#beak和continue
f = 1
while f < 10:
    f += 1
    if (f % 2 != 0):
        continue
    print("f = " + str(f))
g = 1
while 1:
    g += 1
    print(g)
    if(g > 10):
        break

#for
#字符串 list遍历
str1 = "hello"
for letter in str1:
    print(letter)
strList1 = ["hehe","haha"]
for str in strList1:
    print(str)
for index in range(len(strList1)):
    print("gg:",strList1[index])
#使用else
for num in range(10,20):
    for i in range(2,num):
        if num % i == 0:
            j = num / i
            print("%d = %d * %d" % (num,i,j))
            break
    else:
        print(num,"是一个质数")

##嵌套循环

i = 2
while( i < 50):
    j = 2
    while(j <= (i/j)):
        if not(i%j):break
        j += 1
    if(j > i/j):print(i,"是素数")
    i += 1
print("goodbye")