#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : cyl
# @Time : 2021/11/19 14:29
import random
from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        left, right = 0, len(nums) - 1
        self.quick_sort(nums, 0, right)
        return nums
    def quick_sort(self, nums, left, right):
        if left > right:
            return
        mid = self.partion(nums, left, right)
        self.quick_sort(nums, left, mid - 1)
        self.quick_sort(nums, mid + 1, right)

    def partion(self, nums, l, r):
        # 随机选择一个数
        index = random.randint(l, r)
        pivot = nums[index]
        # 将选择的数与最左边的数交换
        nums[index], nums[l] = nums[l], nums[index]
        left, right = l, r
        # 双指针遍历
        while left < right:
            while left < right and nums[right] >= pivot: right -= 1
            while left < right and nums[left] <= pivot: left += 1
            nums[left], nums[right] = nums[right], nums[left]
        # 将中间的数与最左边的数交换
        nums[l], nums[left] = nums[left], nums[l]
        return left


if __name__ == '__main__':
    nums = [5,1,1,2,0,0]
    Solution().sortArray(nums)
    for num in nums:
        print(num)