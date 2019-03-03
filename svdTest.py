#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/3/2 13:01
# @Author  : Arrow and Bullet
# @FileName: svdTest.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/qq_41800366
from numpy import *


U, Sigma, VT = linalg.svd([[1, 1], [7, 7]])
print(U)
print(Sigma)
print(VT)

