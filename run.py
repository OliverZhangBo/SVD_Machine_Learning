#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/3/2 13:07
# @Author  : Arrow and Bullet
# @FileName: run.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/qq_41800366
import svdRec
from numpy import *


Data = svdRec.loadExData()
U, Sigma, VT = linalg.svd(Data)
# print(Sigma)


sig3 = mat([[Sigma[0], 0, 0], [0, Sigma[1], 0], [0, 0, Sigma[2]]])
reconData = U[:, :3] * sig3 * VT[:3, :]
# print(reconData)


myMat = mat(svdRec.loadExData())
# ecludSim = svdRec.ecludSim(myMat[:, 0], myMat[:, 4])
# print(ecludSim)
# ecludSim = svdRec.ecludSim(myMat[:, 0], myMat[:, 0])
# print(ecludSim)
#
#
# cosSim = svdRec.cosSim(myMat[:, 0], myMat[:, 4])
# print(cosSim)
# cosSim = svdRec.cosSim(myMat[:, 0], myMat[:, 0])
# print(cosSim)
#
#
# pearsSim = svdRec.pearsSim(myMat[:, 0], myMat[:, 4])
# print(pearsSim)
# pearsSim = svdRec.pearsSim(myMat[:, 0], myMat[:, 0])
# print(pearsSim)

myMat[0, 1] = myMat[0, 0] = myMat[1, 0] = myMat[2, 0] = 4
myMat[3, 3] = 2

recommend = svdRec.recommend(myMat, 2)
# print(recommend)


myMat =mat(svdRec.loadExData2())
recommend = svdRec.recommend(myMat, 1, estMethod=svdRec.svdEst)
# print(recommend)


imgMatrix = svdRec.imgCompress(2)
print(imgMatrix)
