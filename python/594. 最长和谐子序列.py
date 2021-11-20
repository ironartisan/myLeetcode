#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : cyl
# @Time : 2021/11/20 16:12
from typing import List


class Solution:
    def findLHS(self, nums: List[int]) -> int:
        nums.sort()
        i , ans = 0, 0
        for j in range(len(nums)):
            while i < j and nums[j] - nums[i] > 1: i += 1
            if nums[j] - nums[i] == 1:
                ans = max(ans, j - i + 1)
        return ans


if __name__ == '__main__':
    nums = [1, 3, 2, 2, 5, 2, 3, 7]
    ans = Solution().findLHS(nums)
    print(ans)