#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : cyl
# @Time : 2021/11/25 16:46 
from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        ans = 0
        n = len(nums)
        zero = 0
        left, right = 0, 0
        while right < n:
            if nums[right] == 0:
                zero += 1
            while zero > k:
                if nums[left] == 0:
                    zero -= 1
                left += 1
            right += 1
            ans = max(ans, right - left + 1)
        return ans