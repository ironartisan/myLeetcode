#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : cyl
# @Time : 2021/11/25 16:23 
from typing import List


class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return 1
        left, right = 0, 1
        ans = 0
        while right < n:
            if nums[right] <= nums[right - 1]:
                left = right
            ans = max(right - left + 1, ans)
            right += 1
        return ans


if __name__ == '__main__':
    nums = [1,3,5,4,7]
    val = Solution().findLengthOfLCIS(nums)
    print(val)