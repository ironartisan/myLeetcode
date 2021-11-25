#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : cyl
# @Time : 2021/11/24 9:49 
from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left, right = max(weights), sum(weights)
        while left < right:
            mid = left + (right - left) // 2
            if self.check(weights, mid, days): # 若能在days内运送mid重量的包裹
                right = mid
            else:
                left = mid + 1
        return right

    def check(self, weights, mid, days):
        n = len(weights)
        i = 1 # 用于遍历数组元素
        cnt = 1 # 统计天数
        total = weights[0]
        while i < n:
            while i < n and total + weights[i] <= mid:
                total += weights[i]
                i += 1
            total = 0 # 重新开始计数
            cnt += 1 # 天数加1
        return cnt - 1 <= days


if __name__ == '__main__':
    weights = [3, 2, 2, 4, 1, 4]
    D = 3
    val = Solution().shipWithinDays(weights, D)
    print(val)