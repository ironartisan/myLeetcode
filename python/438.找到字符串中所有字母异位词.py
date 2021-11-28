#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : cyl
# @Time : 2021/11/28 22:00

from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        len_s = len(s)
        len_p = len(p)
        if len_s < len_p:return []
        ans = []
        count_s = [0] * 26
        count_p = [0] * 26
        for i in range(len_p):
            count_s[ord(s[i]) - 97] += 1 # 统计s字符
            count_p[ord(p[i]) - 97] += 1 # 统计p字符

        if count_s == count_p: # 开始位置相等
            ans.append(0)

        for i in range(len_s - len_p): # 移动窗口
            count_s[ord(s[i]) - 97] -= 1
            count_s[ord(s[i + len_p]) - 97] += 1
            if count_s == count_p:
                ans.append(i + 1)
        return  ans


