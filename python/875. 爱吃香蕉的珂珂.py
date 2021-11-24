#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : cyl
# @Time : 2021/11/24 16:23 
from typing import List
import math

class Solution:
    """
    1. 确定k的取值范围
      1.1 数组的最大值
    2. 找出满足H小时的速度k
    """
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        while left < right:
            mid = left + (right - left) // 2
            if self.check(piles, mid, h):
                right = mid
            else:
                left = mid + 1
        return right

    def check(self, piles, mid, h):
        n = len(piles)
        i = 0
        total = 0
        while i < n:
            total += math.ceil(piles[i] / mid)
            i += 1
        return total <= h


if __name__ == '__main__':
    piles = [30,11,23,4,20]
    H = 6
    speed = Solution().minEatingSpeed(piles, H)
    print(speed)
