#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : cyl
# @Time : 2021/11/19 16:15
from typing import List


class Solution:
    def merge(self, A: List[int], m: int, B: List[int], n: int) -> None:
        """
        Do not return anything, modify A in-place instead.
        """
        x, y = m - 1, n - 1
        tail = m + n -1
        while x >= 0 or y >= 0:
            if x == -1: # A先空
                A[tail] = B[y]
                y -= 1
            elif y == -1: # B先空
                A[tail] = A[x]
                x -= 1
            elif A[x] > B[y]: # A > B
                A[tail] = A[x]
                x -= 1
            else: # A < B
                A[tail] = B[y]
                y -= 1
            tail -= 1


if __name__ == '__main__':
    A = [1, 2, 3, 0, 0, 0]
    m = 3
    B = [2, 5, 6]
    n = 3
    Solution().merge(A, m, B, n)
    print(A)