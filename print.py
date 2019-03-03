#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/3/2 17:13
# @Author  : Arrow and Bullet
# @FileName: print.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/qq_41800366
A = 1
B = 2
C = 3
print(A, B, C)  # 1 2 3

D = [1, 2, 3]
for i in D:
    print(i)
# 默认打印结果如下
# 1
# 2
# 3

E = [1, 2, 3]
for i in E:
    print(i, end=" ")
# 现在打印结果如下
# 1 2 3

F = [1, 2, 3]
for i in F:
    print(i, end="！")
# 现在打印结果如下，甚至还可以自定义
# 1！2！3！
