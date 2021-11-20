#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : cyl
# @Time : 2021/11/20 9:37
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        low, high = 0, len(nums) -1
        while True:
            index = self.partion(nums, low, high)
            if index == k - 1:
                return nums[index]
            elif index < k - 1:
                low = index + 1
            else:
                high = index - 1

    def partion(self, nums, low, high):
        pivot = nums[low]
        while low < high:
            while low < high and nums[high] <= pivot: high -= 1 # 若右指针元素小于等于基准值，右指针左移
            nums[low] = nums[high] # 交换元素
            while low < high and nums[low] >= pivot: low += 1 # 若左指针元素大于等于基准值，左指针右移
            nums[high] = nums[low] # 交换元素
        nums[low] = pivot
        return low


if __name__ == '__main__':
    nums = [3,2,1,5,6,4]
    k = 2
    val = Solution().findKthLargest(nums, k)
    print(val)
