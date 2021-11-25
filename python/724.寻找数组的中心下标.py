#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : cyl
# @Time : 2021/11/16 11:40
from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        _sum = sum(nums)
        prefix_sum = [0] * len(nums)
        prefix_sum[0] = nums[0]
        if _sum == prefix_sum[0]:
            return 0
        for i in range(1, len(nums)):
            prefix_sum[i] = nums[i] + prefix_sum[i -1]
            if _sum - prefix_sum[i] == prefix_sum[i - 1]:
                return i
        return -1

    def pivotIndex2(self, nums: List[int]) -> int:
        _sum = sum(nums)
        left_sum = 0
        for i in range(len(nums)):
            if left_sum == _sum - left_sum - nums[i]:
                return i
            left_sum += nums[i]
        return -1

if __name__ == '__main__':
    # nums = [1, 7, 3, 6, 5, 6]
    nums = [2,1,-1]
    index = Solution().pivotIndex(nums)
    print(index)