#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys 

#函数相关
#help 查看帮助
help(int)

#max函数
help(max)
print('实验max')
list1 = [
    [1,4,5,3],
    set([1,4,2,3,4,2]),
    {3:1,5:5,8:'1'},
    (4,2,5,1),
]

for i in list1:
    print(i,'中最大的是：',max(i))

#转型函数不赘述啦

#把函数引用赋值给其他的变量
myHelp = help
myHelp(myHelp)
#你也可以把内置函数给干掉
help = 1
print('help现在不是help了:',help)
print('但我们还是可以用myHelp:',myHelp)
help = myHelp

#重新封装内置函数
myPrint = print
def print(value, *args , sep=' ', end='\n', file=sys.stdout):
    myPrint(' ')
    myPrint(value, *args ,sep=sep, end=end, file=file)

#现在我们有一个全新的print函数了，每次都会折行输出
print('我是大傻逼',"asdfasdga")

#isinstance用来检查对象类型，接受一个class类型参数，或者一个类型元表
print('1的类型为int：',isinstance(1,int))
print('1的类型为int,float中的一个：',isinstance(1,(int,float)))

#多返回值,返回一个元表
def mutipleRet():
    return 1,2,3

print('看看这个函数的返回值：',mutipleRet())

#默认参数
def defaultParam(x = 10):
    print('我吃了%d斤饭' % x)

defaultParam(100)
defaultParam()

#默认参数的传值
def defaultParam2(x,y,z=10,u=100):
    print('x:%s  y:%s  z:%s  u:%s' % (x,y,z,u))

defaultParam2(1,2)

defaultParam2(4,3,z = 10,u = 9)
defaultParam2(4,3,10,9) #和上面的调用等价的

defaultParam2(4,3,z = 19)
defaultParam2(4,3,19) #和上面的调用等价的

defaultParam2(4,3,u = 19) #跳过z直接定义u


#默认参数陷阱,我们可以根据list可变的这个特性，把这个参数做成函数的状态记录器
time_called = [0]
def dpTrick(L = time_called):
    L[0] = L[0] + 1
    #做点什么
    print('调用了%d次函数' % L[0])

dpTrick()
dpTrick()
dpTrick()
dpTrick()
dpTrick()

print('相当于存储了这个函数的一些状态：',time_called)

#可变参数，上面改造print的时候，大家已经见过了
def func1(*alist):
    for i in alist:
        print(i)
    
func1(1,2,3,4)
#or
func1(*[1,2,3,4])

#dict形式的参数
def func2(**params):
    for i in params:
        print(i,':',params.get(i))

func2(a = 1,b = 4,c = 'ff')
func2(**{'a':'b','c':4})

#dic参数不能和参数表中其他的参数名称一样
#参数表顺序必须是 必选参数、默认参数、可变参数、关键字参数 否则会语法错误
def func3(one,two = 2,three = 3,*pa,**params):
    print('one:%s   two:%s   three:%s  other:%s  other2:%s' % (one,two,three,pa,params))

func3(1,2,3,four = 1)

#我用可以用func(*args,**kw)来调用任何函数，填满规则见笔记，可自己测试
func3(*(1,),**{'three':2})