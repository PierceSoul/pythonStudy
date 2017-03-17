t=['name','age','gender']
t2=['liutong',22,'male']
a=1
b=4
c=5
map = {a:'hehe',b:'haha'}
for i in map:
    print(map[i])

map[c] = 'heihei'
print(map)
del(map[c])
sum = 0
for i in  range(0,101):
    sum+=i

print(map.get(2))
if( map.get(2) != None):
    print('hehe')
else:
    print('haha')

print(map.keys())
print(map.values())