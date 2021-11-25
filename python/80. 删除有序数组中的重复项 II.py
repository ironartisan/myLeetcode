#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : cyl
# @Time : 2021/11/25 9:48 


class Solution:
    def removeDuplicates(self, nums) -> int:
        n = len(nums)
        if n <= 2:
            return n
        i = 2
        while i < n:
            if nums[i] == nums[i - 2]:
                nums.pop(i)
            else:
                i += 1
            n = len(nums)
        return n

    def removeDuplicates1(self, nums) -> int:
        n = len(nums)
        if n <= 2:
            return n
        left, right = 2, 2
        while right < n:
            if nums[left - 2] != nums[right]:
                nums[left] = nums[right]
                left += 1
            right += 1
        return left