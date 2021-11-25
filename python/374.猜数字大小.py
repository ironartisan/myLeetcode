#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : cyl
# @Time : 2021/11/23 15:56


def guess(num: int) -> int:
    pass


class Solution:
    def guessNumber(self, n: int) -> int:
        left, right = 1, n
        while left <= right:
            mid = left + (right -left) // 2
            if guess(mid) == 0:
                return mid
            elif guess(mid) == -1:
                right = mid - 1
            else:
                left = mid + 1
