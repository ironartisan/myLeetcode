#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : cyl
# @Time : 2021/11/24 11:05 
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:return -1
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l)// 2
            if nums[mid] == target:
                return mid
            if nums[l] <= nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1