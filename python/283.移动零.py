#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : cyl
# @Time : 2021/11/19 14:30
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index = 0
        m = len(nums) # 统计原数组长度
        for num in nums:
            if num != 0:
                nums[index] = num
                index += 1
        for i in range(index, m):
            nums[index] = 0
            index += 1

    def moveZeroes1(self, nums: List[int]) -> None:
        n = len(nums)
        left = 0
        for right in range(n):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left] # 交换双指针的值
                left += 1

if __name__ == '__main__':
    nums =  [0, 1, 0, 3, 12]
    Solution().moveZeroes(nums)
    for num in nums:
        print(num)
