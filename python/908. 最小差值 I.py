#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : cyl
# @Time : 2021/11/20 17:12
from typing import List

class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        if not nums or len(nums) < 1:
            return 0
        val_max = max(nums)
        val_min = min(nums)
        if val_max - val_min <= 2*k:
            return 0
        else:
            return val_max -val_min - 2*k
