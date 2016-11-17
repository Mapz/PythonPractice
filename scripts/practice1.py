#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#r（大概是real的意思)
a = r"不转义的字符，需要在字符前面加上'r'"

print(a)

#python3下 除法的结果始终为浮点数
a = 3
b = 9
c = b/a
print(c,type(c))

#我们可以看看除法的结果
a = 3.3
b = 9.9
c = b/a
print(c,type(c))

#地板除法重做上面的部分

a = 3
b = 9
c = b//a
print(c,type(c))

a = 3.3
b = 9.9
c = b//a
print(c,type(c))

# python对浮点数大小没有限制，但超过一定大小就表示为inf
bigFloat = 1e11231231231231312
print('bigFloat:',bigFloat)