#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : cyl
# @Time : 2021/11/24 10:49
def isBadVersion(version):
    pass

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 1, n
        while left < right: # 循环直至区间左右端点相同
            mid = left + (right - left) // 2
            if isBadVersion(mid):
                right = mid # 答案在区间 [left, mid] 中
            else:
                left = mid + 1 # 答案在区间 [mid+1, right] 中
        return right # 此时有 left == right，区间缩为一个点，即为答案