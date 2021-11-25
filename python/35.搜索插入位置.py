#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : cyl
# @Time : 2021/11/25 15:56 
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)
        while left < right:
            mid = left + (right -left) // 2
            if nums[mid] == target: # 找到target，直接返回
                return mid
            elif nums[mid] < target: # target在右区间[mid + 1, right)
                left = mid + 1
            else: # target在左区间[left, mid)
                right = mid
        # 分别处理如下四种情况
        # 目标值在数组所有元素之前 [0,0)
        # 目标值等于数组中某一个元素 return middle,即right
        # 目标值插入数组中的位置 [left, right) ，return right 即可
        # 目标值在数组所有元素之后的情况 [left, right)，return right 即可
        return right