#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : cyl
# @Time : 2021/11/20 10:41
import random
from typing import List


class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        self.quick_sort(arr, 0, len(arr) - 1)
        return arr[:k]

    def quick_sort(self, nums,left, right):
        if left > right: return
        mid = self.partion(nums, left, right)
        self.quick_sort(nums, left, mid - 1)
        self.quick_sort(nums, mid + 1, right)

    def partion(self, nums, left, right):
        index = random.randint(left, right)
        pivot = nums[index]
        nums[index], nums[left] = nums[left], nums[index]
        i, j = left, right
        while i < j:
            while i < j and nums[j] >= pivot: j -= 1
            while i < j and nums[i] <= pivot: i += 1
            nums[i], nums[j] = nums[j], nums[i]
        nums[i], nums[left] = nums[left], nums[i]
        return i

if __name__ == '__main__':
    nums = [3, 2, 1, 5, 6, 4]
    k = 2
    numbers = Solution().getLeastNumbers(nums, k)
    print(numbers)
