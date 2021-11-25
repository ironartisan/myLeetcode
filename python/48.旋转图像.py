#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : cyl
# @Time : 2021/11/17 9:40
from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for i in range(n //2): #水平翻转
            for j in range(n):
                matrix[i][j], matrix[n - i -1][j] = matrix[n -i - 1][j], matrix[i][j]
        for i in range(n): # 主对角线翻转
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
