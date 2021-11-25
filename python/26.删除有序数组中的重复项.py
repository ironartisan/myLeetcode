#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : cyl
# @Time : 2021/11/25 10:52 
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2: return n
        left, right = 1, 1
        while right < n:
            if nums[right] == nums[left - 1]:
                right += 1
            else:
                nums[left] = nums[right]
                left += 1
        return left