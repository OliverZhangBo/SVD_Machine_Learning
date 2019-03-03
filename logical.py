#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/3/2 14:49
# @Author  : Arrow and Bullet
# @FileName: logical.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/qq_41800366
from numpy import *

A = [True, True, False, False]
B = [True, False, True, False]
C = logical_xor(A, B)
print(C)  # [False  True  True False]


A = arange(5)
print(A)  # [0 1 2 3 4]
B = logical_xor(A > 1, A > 3)
print(B)  # [False False  True  True False]