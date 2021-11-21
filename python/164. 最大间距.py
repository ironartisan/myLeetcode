#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : cyl
# @Time : 2021/11/21 11:42
from typing import List


class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        nums = self.radixSort(nums)
        return max(nums[i] - nums[i - 1] for i in range(1, len(nums)))

    def radixSort(self, nums):
        for i in range(len(str(max(nums)))):
            buckets = [[] for _ in range(10)] # 创建十进制的二维数组
            for num in nums: # 按照位数的值进行添加到对应的bucket
                buckets[num // (10 ** i) % 10].append(num)
            nums.clear()
            for bucket in buckets: # 按照bucket进行排序
                for num in bucket:
                    nums.append(num)
        return nums