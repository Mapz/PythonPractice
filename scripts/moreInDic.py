#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#keys()取得一个dict的keyset()
dic1 = {1:'x',2:'y',3:'z'}
print('dic1的keyset为：',dic1.keys())
print('他的类型是:',type(dic1.keys()))
print('他是iterable')
for i in dic1.keys():
    print(i)


#可以用values()取得一个dict的valueview
print('dic1的valueview为:',dic1.values())
print('他的类型是:',type(dic1.values()))
print('他是iterable')
for i in dic1.values():
    print(i)

#同时迭代key和value
for item in dic1.items():
    print('%s:%s' % item)
#or
for k,v in dic1.items():
    print('%s:%s' % (k,v))