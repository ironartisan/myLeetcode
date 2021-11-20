#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : cyl
# @Time : 2021/11/20 10:13
from typing import List


class Solution:
    def insert_sort(self, nums:List[int]) -> List[int]:
        for i in range(1, len(nums)):
            key = nums[i]
            j = i -1 # 排好序的最右端元素
            while j >= 0 and nums[j] > key: # 若元素大于key,则将元素右移，直至找到合适的位置
                nums[j + 1] = nums[j]
                j -= 1
            nums[j + 1] = key # 将元素插入到合适位置
        return nums


if __name__ == '__main__':
    nums = [1, 0, 3, 5, 2, 4]
    nums = Solution().insert_sort(nums)
    print(nums)
