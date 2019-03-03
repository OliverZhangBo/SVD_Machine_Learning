#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/3/2 13:05
# @Author  : Arrow and Bullet
# @FileName: svdRec.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/qq_41800366
from numpy import *
from numpy import linalg as la


def loadExData():
    return [[1, 1, 1, 0, 0],
            [2, 2, 2, 0, 0],
            [1, 1, 1, 0, 0],
            [5, 5, 5, 0, 0],
            [1, 1, 0, 2, 2],
            [0, 0, 0, 3, 3],
            [0, 0, 0, 1, 1]]


def loadExData2():
    return[[0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 5],
           [0, 0, 0, 3, 0, 4, 0, 0, 0, 0, 3],
           [0, 0, 0, 0, 4, 0, 0, 1, 0, 4, 0],
           [3, 3, 4, 0, 0, 0, 0, 2, 2, 0, 0],
           [5, 4, 5, 0, 0, 0, 0, 5, 5, 0, 0],
           [0, 0, 0, 0, 5, 0, 1, 0, 0, 5, 0],
           [4, 3, 4, 0, 0, 0, 0, 5, 5, 0, 1],
           [0, 0, 0, 4, 0, 4, 0, 0, 0, 0, 4],
           [0, 0, 0, 2, 0, 2, 5, 0, 0, 1, 2],
           [0, 0, 0, 0, 5, 0, 0, 0, 0, 4, 0],
           [1, 0, 0, 0, 0, 0, 0, 1, 2, 0, 0]]


# 直接利用欧式距离计算相似度
def ecludSim(inA, inB):
    return 1/(1 + la.norm(inA - inB))


# 利用皮尔逊相关系数计算相似度
def pearsSim(inA, inB):
    if len(inA) < 3:
        # 在皮尔逊中，如果向量少于3个点，这时直接判定为两个向量完全相关
        return 1
    return 0.5 + 0.5 * corrcoef(inA, inB, rowvar=0)[0][1]


# 余弦相似度 计算相似度
def cosSim(inA, inB):
    num = float(inA.T * inB)
    denom = la.norm(inA) * la.norm(inB)
    return 0.5 + 0.5*(num/denom)


# 基于物品相似度的推荐系统
def standEst(dataMat, user, simMeas, item):
    n = shape(dataMat)[1]  # 物品数量
    simTotal = 0  # 相似度总量
    ratSimTotal = 0  # 评分相似度
    for j in range(n):  #
        userRating = dataMat[user, j]  # 用户对第j个物品的评价
        if userRating == 0:  #
            continue
        overLap = nonzero(logical_and(dataMat[:, item].A > 0, dataMat[:, j].A > 0))[0]
        # print(nonzero(logical_and(dataMat[:, item].A > 0, dataMat[:, j].A > 0)))
        # print(overLap)
        # 现在终于清楚了，logical_and返回的是布尔值没错
        # nonzero() 返回的是包含非零值对应的下标的元祖
        # overLap 就是包含非零值对应的下标的列表
        if len(overLap) == 0:
            similarity = 0
        else:
            similarity = simMeas(dataMat[overLap, item], dataMat[overLap, j])
        # print("the %d and %d similarity is: %f" % (item, j, similarity))
        simTotal += similarity
        ratSimTotal += similarity * userRating
    if simTotal == 0:
        return 0
    else:
        return ratSimTotal/simTotal


def recommend(dataMat, user, N=3, simMeas=cosSim, estMethod=standEst):
    unratedItems = nonzero(dataMat[user, :].A == 0)[1]
    if len(unratedItems) == 0:
        return "you rated everything"
    itemScores = []
    for item in unratedItems:
        estimatedScore = estMethod(dataMat, user, simMeas, item)
        itemScores.append((item, estimatedScore))
    return sorted(itemScores, key=lambda jj: jj[1], reverse=True)[:N]


# 基于SVD的评分估计
def svdEst(dataMat, user, simMeas, item):
    n = shape(dataMat)[1]
    simTotal = 0
    ratSimTotal = 0
    U, Sigma, VT = la.svd(dataMat)
    Sig4 = mat(eye(4) * Sigma[:4])
    xformedItems = dataMat.T * U[:, :4] * Sig4.I
    for j in range(n):
        userRating = dataMat[user, j]
        if userRating == 0 or j == item:
            continue
        similarity = simMeas(xformedItems[item, :].T, xformedItems[j, :].T)
        print("the %d and %d similarity is: %f" % (item, j, similarity))
        simTotal += similarity
        ratSimTotal += similarity * userRating
    if simTotal == 0:
        return 0
    else:
        return ratSimTotal/simTotal


def printMat(inMat, thresh=0.8):
    for i in range(32):
        for j in range(32):
            if float(inMat[i, j]) > thresh:
                print(1, end=" ")
            else:
                print(0, end=" ")
        print(" ")


def imgCompress(numSV=3, thresh=0.8):
    my1 = []
    # for line in open("./data/0_5.txt").readlines():
    #     newRow = []
    #     for i in range(32):
    #         newRow.append(int(line[i]))
    #     my1.append(newRow)
    # myMat = mat(my1)
    # # 上面代码简写
    myMat = mat(([list(map(int, [i for i in line.strip()])) for line in open("./data/0_5.txt").readlines()]))
    print(myMat)
    print("****original matrix******")
    printMat(myMat, thresh)
    U, Sigma, VT = la.svd(myMat)
    SigRecon = mat(zeros((numSV, numSV)))
    for k in range(numSV):
        SigRecon[k, k] = Sigma[k]
    reconMat = U[:, :numSV] * SigRecon * VT[:numSV, :]
    print("****reconstructed matrix using %d singular values*****" % numSV)
    printMat(reconMat, thresh)
