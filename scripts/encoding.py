#!/usr/bin/env python3
# -*- coding: utf-8 -*-


#chr() 和 ord()
a = '天'
print( a,'的unicode十进制数:',ord(a))
b = 22950
print('unicode十进制数为',b,'的字符:',chr(b))


#用十六进制编码表示字符串，可用转义符 _*\u + 十六进制编码*_ 例如 '\u4e2d\u6587'
c = '\u4e2d\u6587'
print(r'\u4e2d\u6587','表示字符串：',c) 

#byte形式,可用b表示，但只对ascii能表示的内容有效
d = b'abc' #正确
#d = b'中文' 错误
print("byte形式:",d)

#非ascii文字，使用.encode(编码)来byte化，当然ascii文字也可以..
str0 = 'abc'
encodings = ['ascii','gbk','utf-8']
for encoding in encodings:
    print(str0,'用',encoding,'编码后为：',str0.encode(encoding))

#非ascii文字，使用.encode(编码)来byte化，当然，这时候不能用'ascii'来encode了
encodings = encodings[1:]
str1 = 'Python学习'
for encoding in encodings:
    print(str1,'用',encoding,'编码后为：',str1.encode(encoding))
#输出结果可以看书，gbk汉字占2个字节，utf-8一般3个字节

#使用decode来解码，解码的时候要保持编码一致，不然会出乱码
str2 = 'Mapz的python学习'
encoding1 = 'utf-8'
encoding2 = 'gbk'
e = str2.encode(encoding1)
print(str2,'编码为',encoding1,":",e)
print(e,'用',encoding1,'解码：',e.decode(encoding1))
#如果解码对不上，会出乱码
print(e,'用',encoding2,'解码：',e.decode(encoding2))

#字符串格式化
f = '%s今天吃了%d个包子，重了%f斤' %('我',2,0.3)
print('格式化输出1：',f)
#尝试修改小数位数，让显示的好看点，%.xf表示保留到小数点后x位
f = '%s今天吃了%d个包子，重了%.1f斤' %('我',2,0.35)
print('格式化输出2：',f)
#整数可以补0和空格,%0xd代表整数用0补到x位,%xd表示用空格补齐到x位
f = '%03d一步可以跳出%4d个空格远' %(7,3)
print('整数补0和空格：',f) 


#len的使用
print('字符串 %s 的长度为 %d'%(str2,len(str2)))
print('字符串 %s 转换为utf-8后的大小为 %d 字节' %(str2,len(str2.encode('utf-8'))))





