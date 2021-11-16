#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : cyl
# @Time : 2021/11/16 15:00
from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        nums[:n - k] = list(reversed(nums[:n - k]))
        nums[n - k:] = list(reversed(nums[n - k:]))
        nums.reverse()



if __name__ == '__main__':
    nums =  [1,2,3,4,5,6,7]
    k = 3
    Solution().rotate(nums, k)
    for num in nums:
        print(num)