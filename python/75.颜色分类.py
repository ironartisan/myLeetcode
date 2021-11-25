#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : cyl
# @Time : 2021/11/20 8:50
from typing import List
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        index = 0
        for i in range(n):
            if nums[i] == 0:
                nums[index], nums[i] = nums[i], nums[index]
                index += 1
        for j in range(index, n):
            if nums[j] == 1:
                nums[index], nums[j] = nums[j], nums[index]
                index += 1

    def sortColors1(self, nums: List[int]) -> None:
        n = len(nums)
        left, right = 0, n - 1
        i = 0
        while i <= right:
            # 这里不能是if nums[i] == 2,考虑到特殊情况nums = [2,1,2]
            while i < right and nums[i] == 2:
                nums[i], nums[right] = nums[right], nums[i]
                right -= 1
            if nums[i] == 0:
                nums[i], nums[left] = nums[left], nums[i]
                left += 1
            i += 1


if __name__ == '__main__':
    # nums = [2, 0, 2, 1, 1, 0]
    nums =  [2,1,2]
    Solution().sortColors1(nums)
    print(nums)
