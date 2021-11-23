#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : cyl
# @Time : 2021/11/23 16:36

class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 1,  x // 2 + 1
        while left <= right:
            mid = left + (right - left) // 2
            if mid * mid < x:
                left = mid + 1
            elif mid * mid > x:
                right = mid - 1
            else:
                return mid
        return right # 取右边界，向下取整