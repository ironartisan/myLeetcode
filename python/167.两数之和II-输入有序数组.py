#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : cyl
# @Time : 2021/11/23 21:14

from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left <= right:
            val = numbers[left] + numbers[right]
            if val == target:
                return [left + 1, right + 1]
            elif val < target:
                left += 1
            else:
                right -= 1
        return []
