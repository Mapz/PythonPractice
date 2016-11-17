#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#条件语句和循环

#条件

#各种空元素
empties = [
    '',
    [],
    (),
    {},
    set([]),
    0,
]

#各种非空元素
nonEmpties = [
    '1',
    ['1'],
    (1,),
    {"1":1},
    set(['1']),
    1,
]

print('各种空元素：',empties)
print('各种非空元素：',nonEmpties)

#各种空元素作逻辑判断时候为False
for element in empties:
    print('元素',element,':')
    if element:
        print(True)
    else:
        print(False)

#各种非空元素作逻辑判断时候为True
for element in nonEmpties:
    print('元素',element,':')
    if element:
        print(True)
    else:
        print(False)

#不执行后面的
def retX(x):
    print(x)
    return x

if retX(0): #False 会继续执行
    pass
elif retX(1): #True 后面的条件不执行了
    pass
elif retX(2): #不执行判断
    pass
else:   
    pass

#range()
rg1 = range(3)
print('rg1是一个range对象，值为:%s\n类型是:%s\n可用list(rg1)转为list:%s' % (rg1,type(rg1),list(rg1)))

rg2 = range(10,15)
print('range接受2个参数的时候分别表示开始和结束(until)例如rg2为 %s , 转换为list为 %s' % (rg2,list(rg2)))

#循环（和遍历是一样的）
#用list
print(' ')
print('list循环')
for i in [1,2,3]:
    print(i)

print(' ')
print('range循环')
#用range
for i in range(10,15):
    print(i)

#遍历和循环的方式类似的
print(' ')
print('set遍历')
#对set的遍历是无序的，因为set是无序
for i in set([5,6,1,2,3]):
    print(i)

print(' ')
print('dic遍历')
#对dic的遍历 是遍历的keyset
dic1 = {1:'one',2:'two'}
for i in dic1:
    print(i,':',dic1.get(i))

print(' ')
print('while循环')
#while循环
n = 0
while n<5:
    print(n)
    n += 1
    
#退出循环
print(' ')
print('寻找dic中value为某值的key')
dic2 = {1:'wrong',2:'wrong',3:'wrong',4:'right',5:'wrong'}
for key in dic2:
    print('正在遍历:%s' % key)
    if dic2.get(key) == 'right':
        print('正确的key为:%s' % key)
        break
    
print(' ')
print('continue的使用')
#跳到下个循环
for key in dic2:
    if dic2.get(key) == 'wrong':
        continue
    print('我只要正确的循环：%s' % key)


#查看对象是否iterable
from collections import Iterable
def isIterable(obj):
    print('对象%s是否可遍历：%s' % (obj,isinstance(obj,Iterable)))

isIterable([1,2,3,4])
isIterable(())
isIterable({})
isIterable('1234')
isIterable(1234)

#enumerate，要注意dic1 得到的 还是 keyset的处理
dic1 = {'x':'1','y':'2','z':'3'}
str1 = '1234567'
list1 = list(str1)
set1 = set(list1)

def enumerateOut(obj):
    for i,v in enumerate(obj):
        print("enumerate输出：%s:%s" % (i,v))

print('dic1')
enumerateOut(dic1)
print('str1')
enumerateOut(str1)
print('list1')
enumerateOut(list1)
print('set1')
enumerateOut(set1)

#迭代内容只有一个元素的时候，是一个元素，如果是多个，则是一个tuple
#迭代的变量和元素赋值的时候一样，用多个变量来赋值，会把tuple中的值赋给每个变量
#如果只有一个迭代的遍历，则会把整个tuple赋值给他
for x in [(1, 1), (2, 4), (3, 9)]:
    print(x) #x是个tuple

for x,y in [(1, 1), (2, 4), (3, 9)]:
    print(x,y) #x是个tuple
