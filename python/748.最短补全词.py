#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : cyl
# @Time : 2021/12/10 16:35
from collections import Counter
from typing import List


class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        cnt = Counter(ch.lower() for ch in licensePlate if ch.isalpha())
        res = []
        for word in words:
            if not cnt - Counter(word):
                res.append(word)
        return min(res, key=len)

