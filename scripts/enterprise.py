#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#slice 切片

a = [1,2,3,4,5,6,7,8,9,10]

print(a[5:])
print(a[5:-1])
print(a[-3:])
print(a[:-3])
print(a[::2])
print(a[1::2])

b = (1,2,3,4,5,6,7,8,9,10)

print(b[5:])
print(b[5:-1])
print(b[-3:])
print(b[:-3])
print(b[::2])
print(b[1::2])

c = '123456789'

print(c[5:])
print(c[5:-1])
print(c[-3:])
print(c[:-3])
print(c[::2])
print(c[1::2])

a1 = a[:]
b1 = b[:]
c1 = c[:]

print(a1 is a)
print(b1 is b)
print(c1 is c)

