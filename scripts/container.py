#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#list 列表

list1 = ['1','2','3','4']

list1.append('5')
print('加上5：',list1)

list1.insert(1,'捣乱的')
print('在位置1插入捣乱的：',list1)

#下标从0开始，负数为倒数方式
print('第0个元素是:',list1[0])
print('第1个元素是:',list1[1])
print('倒数第1个元素是:',list1[-1])
print('倒数第2个元素是:',list1[-2])

#pop为退出元素，带下标参数为退出下标元素
print('退出最后一个元素:',list1.pop(),'\n剩下了：',list1)
print('退出第一个元素:',list1.pop(1),'\n剩下了：',list1)

#存在的元素可以直接赋值替换
list1[2] = '我还是3'
print('第二个元素被替换了:',list1)

# list1[4] = '5'  错误，不存在的元素不能被替换


#tuple tuple初始化后是不能修改的
tuple1 = (1,2,3)
print('元组1:',tuple1)
print('元组1第一个元素:',tuple1[1])

#空的tuple
tuple2 = ()
print('空元组:',tuple2,'\n长度为:',len(tuple2))

#一个元素的tuple要注意第0个元素后面加逗号，打印的时候也会被多一个逗号
not_tuple3 = (1)
tuple3 = (1,)
print('只有一个元素的元组:',tuple3,'\n长度为:',len(tuple3))
print('(1)这个不会成为一个tuple：',not_tuple3)

#字典 dict
dic1 = {1:40,'map':'42',True:123}
print("取元素1:",dic1[1])
print("取元素mapz:",dic1['map'])
print("取元素True:",dic1[True])

#打印字典
print("dic1内容：",dic1)

#可以用赋值的方式直接加入新元素
dic1[False] = 433
print('加入的False为：',dic1[False])

print("dic1内容：",dic1)

#直接取不存在的元素会keyError
# print("不存在的元素：",dic1['unknown'])
# Traceback (most recent call last):
#   File "/Volumes/store/Store/PythonPractice/scripts/container.py", line 57, in <module>
#     print("不存在的元素：",dic1['unknown'])
# KeyError: 'unknown'

#用in 或者 get 来避免报错
if False in dic1:
    print("False在dic1中，值为：",dic1[False])
if not '不存在' in dic1:
    print('不存在 不在 dic1中')

#或者

print('看看False是否在dic1：',dic1.get(False,'不存在'))
print(r'看看"不存在"是否在dic1：',dic1.get('不存在','不存在'))

#用pop来退出一个元素
print('把False推出来：',dic1.pop(False),"\n退出来后：",dic1)

#Python中的1和True 0和False
print('True和1是否相等：%s' % (True == 1))
print('False和0是否相等：%s' % (False == 0))

#set 不重复无序集合
set1 = set([1,2,3,4,"5"])
print('set1为:',set1)
set2 = set([1,2,3,4,4,4])
print('通过list构建会过滤掉重复项目:',set2)

#增删元素
set1.add(5)
print('set1增加元素5：',set1)
set1.remove('5')
print('set1删除元素”5“:',set1)

#用set来做并和交操作
set2 = ({'face','key','out'})
set3 = ({'face','key','value'})
print('set2与set3交集：',(set2&set3))
print('set2与set3并集：',(set2|set3))

#可变和不可变对象
str3 = "abc"
str4 = str3.replace('a','A')
print('str3不会变的:%s\n只会有一个新的引用，我们给他赋给str4:%s'%(str3,str4))

list1 = [3,4,2,5,1]
print('list1现在是这样:%s' % list1)
print('list1地址为:',id(list1))
list1.sort()
print('list1现在内容变了:%s' % list1)
print('但是list1的地址没有变:',id(list1))

