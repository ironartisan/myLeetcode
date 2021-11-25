#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : cyl
# @Time : 2021/11/25 9:15
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums or len(nums) < 3: return []
        n = len(nums)
        nums.sort()
        ans = []
        for i in range(n):
            if nums[i] > 0: break
            if i > 0 and nums[i] == nums[i - 1]: continue
            left, right = i + 1, n-1
            while left < right:
                _sum = nums[i] + nums[left] + nums[right]
                if _sum > 0: right -= 1
                elif _sum < 0: left += 1
                else:
                    ans.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[right] == nums[right - 1]:right -= 1
                    while left < right and nums[left] == nums[left + 1]: left += 1
                    right -= 1
                    left += 1
        return ans


if __name__ == '__main__':
    nums = [-1, 0, 1, 2, -1, -4]
    three_sum = Solution().threeSum(nums)
    print(three_sum)
