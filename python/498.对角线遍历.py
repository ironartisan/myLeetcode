#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : cyl
# @Time : 2021/11/17 11:44
from typing import List

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]:
            return []
        m, n = len(mat), len(mat[0])
        j, k = 0, 0
        count = m + n - 1
        index = 0
        res = [0] * (m * n)
        for i in range(count):
            if i % 2 == 0: # 右上方向
                while j >= 0 and k < n:
                    res[index] = mat[j][k]
                    index += 1
                    j -= 1
                    k += 1
                if k < n: # 边界情况1
                    j += 1
                else: # 边界情况2
                    j += 2
                    k -= 1
            else: # 左下方向
                while j < m and k >= 0:
                    res[index] = mat[j][k]
                    index += 1
                    j += 1
                    k -= 1
                if j < m: # 边界情况1
                    k += 1
                else:  # 边界情况2
                    j -= 1
                    k += 2
        return res


if __name__ == '__main__':
    mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    res = Solution().findDiagonalOrder(mat)
    for num in res:
        print(num)
