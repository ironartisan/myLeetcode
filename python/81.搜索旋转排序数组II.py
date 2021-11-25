#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : cyl
# @Time : 2021/11/24 15:48 
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if not nums: return -1
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return True
            if nums[l] < nums[mid]:  # 若mid左边有序
                if nums[l] <= target <= nums[mid]:  # 判断target是否在[left, mid]中
                    r = mid - 1
                else:
                    l = mid + 1
            elif nums[l] > nums[mid]:  # 若mid右边有序
                if nums[mid] < target <= nums[r]:  # 判断target是否在[mid + 1, right]中
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                if nums[l] == target:
                    return True
                else:
                    l += 1
        return False