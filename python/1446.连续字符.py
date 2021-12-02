#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : cyl
# @Time : 2021/12/1 8:43 

class Solution:
    def maxPower(self, s: str) -> int:
        if len(s) < 2: return len(s)
        res = 0
        count = 1
        for i in range(1, len(s)):
            if s[i - 1] == s[i]:
                count += 1
            else:
                count = 1
            res = max(res, count)
        return res