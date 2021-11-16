#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : cyl
# @Time : 2021/11/16 10:41
from typing import List


class solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        for i in range(n - 1, -1, -1): #逆序遍历
            digits[i] += 1
            if digits[i] <= 9: return digits # 若满足条件，则直接返回
            digits[i] = 0
        digits.insert(0, 1) # 特殊情况
        return digits

    def plusOne2(self, digits: List[int]) -> List[int]:
        n = len(digits)
        for i in range(n - 1, -1, -1):
            if digits[i] != 9:
                digits[i] += 1
            for j in range(i + 1, n):
                digits[j] = 0
            return digits
        return [1] + [0] * n
